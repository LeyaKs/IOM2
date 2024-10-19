from flask import Flask, request, send_file, render_template
import os
import json
from src.data_grouped import group

HDRS = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # func when located in root
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    if 'file' not in request.files or file.filename == '':
      return render_template('not_chosen.html')
    
    input_file_path = os.path.join('uploads', file.filename)
    file.save(input_file_path)  # save file it is uploaded
    array = group(file)  # convert file, return array of dicts for each question
    rep(array)
    return render_template('report.html')  # page if file is uploaded
  return render_template('index.html')


def rep(array):
  workers = ["Работа", "Зарплата", "Менеджмент", "Возможности роста", 
  "Атмосфера", "Перегрузка", "Условия труда", "Стабильность", "Честность",
  "Условия конкурентов привлекательнее", "Негативные эмоции", "Позитивные эмоции"]
  personal = ["Переезд", "Семья", "Обучение", "Здоровье", "Ценности", "Приоритеты", "Неудовлетворение"]
  simple_answers = ["Да", "Нет"]
  ind = 0     # diagram index
  ind_list = 0  # question index
  with open("templates/report_sample.txt", 'r+', encoding='utf-8') as infile, open("templates/report.html", 'w', encoding='utf-8') as outfile:  #Открытие шаблона txt и преобразование его в html
    for line in infile:  # iterating through lines in template html file
      keys = list(array[ind_list].keys())  # keys(reasons) array
      values = list(array[ind_list].values()) # values(frequencies) array
      match(ind):
        case 1:
          result = create_list(keys, values, personal)  # a diagram with personal reasons
        case 2:  
          result = create_list(keys, values, workers)   # a diagram with general reasons
        case 3 | 4 | 5:
          result = create_list(keys, values, personal + workers + simple_answers)   # diagrams for 2, 3, 4 questions
        case _:
          result = create_list(keys, values, personal + workers)  # diagrams for 1 question
          
      str_keys = result[0][:-3]   # deleting ," in the end
      str_values = result[1][:-2] # deleting commas in the end
      line = line.replace(f'@k{ind+1}', str_keys) # insterting keys instead of a label in template
      line = line.replace(f'@v{ind+1}', str_values) # insterting values instead of a label in template
      if str_values in line and ind_list != len(array):
        ind += 1
        if (ind > 2):
          ind_list += 1
      outfile.write(line)

def create_list(keys, values, arr) -> tuple[str, str]:
  str_keys = "\""     # creating a keys string for a diagram
  str_values = ""     # creating a values string for a diagram
  for index in range(len(keys)):
    for j in range(len(arr)): 
      if keys[index] in arr[j] and values[index] >= 3: # check that there are not less than 3 entries
          str_keys += keys[index]
          str_keys += '" , "'
          str_values += str(values[index])
          str_values += ' , ' 
  return [str_keys, str_values]

def init_dir(filename):
    if not os.path.exists(filename):
        os.makedirs(filename)

if __name__ == '__main__':
  init_dir('uploads')
  app.run(host='0.0.0.0', debug=True)
