FROM python:3.10-alpine

RUN apk add --no-cache socat
RUN pip install pycryptodome sympy
ENV PYTHONUNBUFFERED=1

COPY server.py /src/
COPY flag.txt /src/
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
