FROM python:3.11-alpine

RUN apk add --no-cache socat
ENV PYTHONUNBUFFERED=1

COPY server.py /src/server.py
COPY flag.txt /src/flag.txt
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
