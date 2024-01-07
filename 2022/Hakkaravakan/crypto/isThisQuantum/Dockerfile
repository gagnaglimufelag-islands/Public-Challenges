FROM python:3.10-alpine

RUN apk add --no-cache socat gcc g++ make libffi-dev openssl-dev
RUN pip install PyCryptodome
ENV PYTHONUNBUFFERED=1

COPY serverUncensored.py /src/server.py
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
