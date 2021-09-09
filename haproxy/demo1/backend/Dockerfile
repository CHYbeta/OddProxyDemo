#FROM node:12.18.1
#RUN mkdir -p /backend
#COPY . /backend
#WORKDIR /backend

FROM python:3.6.7

RUN mkdir -p /backend
COPY . /backend
WORKDIR /backend

RUN python3 -m pip install -r requirements.txt
