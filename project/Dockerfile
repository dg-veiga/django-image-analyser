FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/project

RUN apt-get update &&\
    apt-get install -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .