FROM python:3.7

MAINTAINER Alex Petrov<apetrov@appgrowth.com>

RUN apt-get update

COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt

