from flask import Flask, request, send_file, render_template
import os

HDRS = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if (not file) & ('file' not in request.files or file.filename == ''):
            return 'Файл не выбран'
        return render_template('report.html')
    return render_template('index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
