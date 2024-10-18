from flask import Flask, request, send_file, render_template
import os
import json

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

    array = [{'A':24, 'B':64}, {'A1':25, 'B1':64}]  
    rep(array)
    # Передача данных в JSON-формате в HTML
    #chart_data_json = json.dumps(chart_data)
    
    return render_template('report.html')


  return render_template('index.html')



def rep(array):
  ind = 1
  with open("templates/report_sample.html", 'r+', encoding='utf-8') as infile, open("templates/report.html", 'w', encoding='utf-8') as outfile:
    for line in infile:
      
      keys = list(array[ind-1].keys())
      values = list(array[ind-1].values())
      str_keys = ""
      str_values = ""
      switch(ind):
        case 2:
          for index in range(0,11):
            str_keys += keys[index]
            if key != keys[10]:
              str_keys += '" , "'
            str_values += values[index]
            if value != values[10]:
              str_values += ' , '  
          break;
        case 3:
          for index in range(11,18):
            str_keys += keys[index]
            if key != keys[17]:
              str_keys += '" , "'
            str_values += values[index]
             if value != values[17]:
              str_values += ' , '  
          break;
        default:
          for key in keys:
            str_keys += key
            if key != keys[-1]:
              str_keys += '" , "'
          for value in values:
            str_values += str(value)
            if value != values[-1]:
              str_values += ' , '    
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
