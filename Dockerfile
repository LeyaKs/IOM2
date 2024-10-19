FROM python:latest
COPY . /
RUN  pip3 install --upgrade pip && pip install --upgrade setuptools && pip3 install -r /requirements.txt && chmod +x /main.py


CMD [ "python3", "/main.py" ]