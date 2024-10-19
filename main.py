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
    print(array)
    rep(array)
    # Передача данных в JSON-формате в HTML
    #chart_data_json = json.dumps(chart_data)
    
    return render_template('report.html')


  return render_template('index.html')



def rep(array):
  workers = ("Работа", "Зарплата", "Менеджмент", "Возможности роста", 
  "Атмосфера", "Перегрузка", "Условия труда", "Стабильность", "Честность",
  "Условия конкурентов привлекательнее", "Негативные эмоции")
  personal = ("Переезд", "Семья", "Обучение", "Здоровье", "Ценности", "Приоритеты", "Неудовлетворение")
  ind = 1
  with open("templates/report_sample.html", 'r+', encoding='utf-8') as infile, open("templates/report.html", 'w', encoding='utf-8') as outfile:
    for line in infile:
      
      keys = list(array[ind-1].keys())
      values = list(array[ind-1].values())
      str_keys = "\""
      str_values = ""
      match(ind):
        case 2:
          for index in range(len(keys)):
            if keys[index] in personal:
              str_keys += keys[index]
              str_keys += '" , "'
              str_values += str(values[index])
              str_values += ' , ' 
        case 3:  
          for index in range(len(keys)):
            if keys[index] in workers:
              str_keys += keys[index]
              str_keys += '" , "'
              str_values += str(values[index])
              str_values += ' , '     
        case _:
          for index in range(len(keys)):
            if keys[index] in workers or keys[index] in personal:
              str_keys += keys[index]
              str_keys += '" , "'
              str_values += str(values[index])
              str_values += ' , '   
      str_keys = str_keys[:-3]
      str_values = str_values[:-3]
      print(ind)
      print(len(array))
      line = line.replace(f'@k{ind}', str_keys)
      line = line.replace(f'@v{ind}', str_values)
      if str_values in line and ind != len(array):
        ind += 1

      outfile.write(line)

def init_dir(filename):
    if not os.path.exists(filename):
        os.makedirs(filename)

if __name__ == '__main__':
  init_dir('uploads')
  app.run(host='0.0.0.0', debug=True)
