FROM python:3.12-alpine

RUN apk add --no-cache socat
ENV PYTHONUNBUFFERED=1

COPY src/chall.py /src/chall.py
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python chall.py'
