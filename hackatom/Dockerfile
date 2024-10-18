FROM python:3.9.20-slim
COPY . /
RUN  pip3 install --upgrade pip && python3 -m venv .hackaton \
        source ./hackaton/bin/activate && pip3 install -r /requirements.txt && chmod +x /main.py


CMD [ "python3", "/main.py" ]