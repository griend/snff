# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /opt/snuff

COPY src/python/ .

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m", "hello" ]
