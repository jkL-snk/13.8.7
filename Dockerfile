FROM python:3

COPY script.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "./script.py" ]
