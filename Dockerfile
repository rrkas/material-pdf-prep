FROM ubuntu:22.04

RUN apt-get update && \
    apt update && \
    apt-get install -y python3 python3-pip wget libreoffice

RUN cp /usr/bin/python3 /usr/bin/python

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
