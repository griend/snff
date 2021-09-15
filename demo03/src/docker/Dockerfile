FROM python:3

COPY src/python/ /opt/snff

WORKDIR /opt/snff

RUN pip3 install --no-cache-dir --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD gunicorn -w 5 -b 0.0.0.0:5000 --access-logfile=- app:app
