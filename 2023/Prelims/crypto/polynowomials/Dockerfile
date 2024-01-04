FROM python:alpine

RUN apk add --no-cache socat
ENV PYTHONUNBUFFERED=1

COPY chall.py /src/
COPY polynomial.py /src/
WORKDIR /src

CMD echo $FLAG > flag.txt && socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python chall.py'
