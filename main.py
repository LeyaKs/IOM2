from flask import Flask, request, send_file, render_template
import os

HDRS = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
   return render_template('index.html')

def init_dir(filename):
  if not os.path.exists(filename):
    os.makedirs(filename)

if __name__ == '__main__':
  init_dir('uploads')
  app.run(host='0.0.0.0', debug=True)
