FROM ubuntu:22.04

ENV TZ="Asia/Kolkata" DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install tzdata -y
RUN apt-get update -y && \
    apt update -y && \
    apt-get install -y python3 python3-pip wget libreoffice \
        sox ffmpeg libcairo2 libcairo2-dev 

# RUN apt-get install -y texlive-full

RUN cp /usr/bin/python3 /usr/bin/python

WORKDIR /tmp

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb && \
    dpkg -i libssl1.0.0_1.0.2n-1ubuntu5_amd64.deb

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
