FROM ubuntu:22.04

ENV TZ="Asia/Kolkata" DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install tzdata -y
RUN apt-get update -y && \
    apt update -y && \
    apt-get install -y python3 python3-pip wget libreoffice \
        sox ffmpeg libcairo2 libcairo2-dev texlive-full


RUN cp /usr/bin/python3 /usr/bin/python

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
