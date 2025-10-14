FROM python:3.12-alpine

RUN apk add --no-cache socat gcc g++ make libffi-dev openssl-dev curl tar xz
ENV PYTHONUNBUFFERED=1

COPY typst.tar.xz .
RUN tar xvf typst.tar.xz -C /tmp && mv /tmp/typst-x86_64-unknown-linux-musl/typst /usr/local/bin/typst

COPY src/server.py /src/server.py
COPY src/flag.txt /src/flag.txt
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
