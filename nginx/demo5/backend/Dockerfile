FROM python:3.6.7

RUN mkdir -p /backend
WORKDIR /backend
COPY requirements.txt /backend
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend