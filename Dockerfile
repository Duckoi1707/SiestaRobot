FROM debian:11
FROM python:3.10.1-slim-buster
FROM nikolaik/python-nodejs:python3.9-nodejs17

WORKDIR /SiestaRobot/
WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install git
RUN python3.9 -m pip install -U pip
RUN apt-get install -y wget python3-pip curl bash neofetch ffmpeg software-properties-common
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY . /app

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

COPY . .
CMD ["python3.9", "-m", "SiestaRobot"]
CMD python3 main.py
