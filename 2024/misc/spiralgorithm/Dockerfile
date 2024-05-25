FROM python:3.12-alpine

RUN apk add --no-cache socat gcc g++ make libffi-dev openssl-dev
ENV PYTHONUNBUFFERED=1

COPY server.py /src/server.py
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
