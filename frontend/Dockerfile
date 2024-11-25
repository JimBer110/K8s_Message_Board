#syntax=docker/dockerfile:1

FROM python:3.12-alpine

WORKDIR /frontend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]