FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /InnoCPC

WORKDIR /InnoCPC
COPY InnoCPC /InnoCPC