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
    
    inp = {'A':24, 'B':64}
    # Передача данных в JSON-формате в HTML
    #chart_data_json = json.dumps(chart_data)
    rep(list(inp.keys()), list(inp.values()))

    return render_template('report.html')


  return render_template('index.html')



def rep(keys, values):
  str_keys = ""
  str_values = ""
  for key in keys:
    str_keys += key
    if key != keys[-1]:
      str_keys += '" , "'
  for value in values:
    str_values += str(value)
    if value != values[-1]:
      str_values += ' , '
  with open("templates/report_sample.html", 'r') as infile, open("templates/report.html", 'w', encoding='utf-8') as outfile:
    for line in infile:
      line = line.replace(f'@k', str_keys)
      line = line.replace(f'@v', str_values)
      outfile.write(line)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
