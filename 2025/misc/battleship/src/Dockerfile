FROM python:3.10-alpine

RUN apk add --no-cache socat gcc g++ make libffi-dev openssl-dev
ENV PYTHONUNBUFFERED=1

COPY game.py /src/game.py
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python game.py'
