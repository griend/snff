FROM python:3

COPY src/python/ /opt/snff

WORKDIR /opt/snff

RUN pip3 install --no-cache-dir --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python3 -m flask run --host=0.0.0.0
