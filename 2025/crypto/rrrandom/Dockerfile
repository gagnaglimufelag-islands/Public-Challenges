FROM python:3.12-alpine

RUN apk add --no-cache socat gcc g++ make libffi-dev openssl-dev curl tar xz
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/server.py .

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
