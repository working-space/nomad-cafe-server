FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /wwwroot
WORKDIR /wwwroot

ADD requirements.txt /wwwroot/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /wwwroot/
