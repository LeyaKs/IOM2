from flask import Flask, request, send_file, render_template
import os
import json
from data_grouped import group

HDRS = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    if 'file' not in request.files or file.filename == '':
      return 'Файл не выбран'
    input_file_path = os.path.join('uploads', file.filename)
    file.save(input_file_path)
    array = group(file)
    rep(array)
    return render_template('report.html')
  return render_template('index.html')


def rep(array):
  workers = ["Работа", "Зарплата", "Менеджмент", "Возможности роста", 
  "Атмосфера", "Перегрузка", "Условия труда", "Стабильность", "Честность",
  "Условия конкурентов привлекательнее", "Негативные эмоции"]
  personal = ["Переезд", "Семья", "Обучение", "Здоровье", "Ценности", "Приоритеты", "Неудовлетворение"]
  ind = 0
  ind_list = 0
  with open("templates/report_sample.html", 'r+', encoding='utf-8') as infile, open("templates/report.html", 'w', encoding='utf-8') as outfile:
    for line in infile:
      
      keys = list(array[ind_list].keys())
      values = list(array[ind_list].values())
      
      match(ind):
        case 1:
          result = create_list(keys, values, personal)
        case 2:  
          result = create_list(keys, values, workers)
        case 3:
          result = create_list(keys, values, personal + workers + ["Да","Нет"])
        case _:
          result = create_list(keys, values, personal + workers)
          
      str_keys = result[0][:-3]
      str_values = result[1][:-2]
      line = line.replace(f'@k{ind+1}', str_keys)
      line = line.replace(f'@v{ind+1}', str_values)
      if str_values in line and ind_list != len(array):
        ind += 1
        if (ind > 2):
          ind_list += 1
      outfile.write(line)

def create_list(keys, values, arr):
  str_keys = "\""
  str_values = ""
  for index in range(len(keys)):
    for j in range(len(arr)): 
      if keys[index] in arr[j] and values[index] > 0:
          str_keys += keys[index]
          str_keys += '" , "'
          str_values += str(values[index])
          str_values += ' , ' 
  return (str_keys, str_values)

def init_dir(filename):
    if not os.path.exists(filename):
        os.makedirs(filename)

if __name__ == '__main__':
  init_dir('uploads')
  app.run(host='0.0.0.0', debug=True)
