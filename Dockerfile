FROM python:3.8.10

ADD ./src /

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]

