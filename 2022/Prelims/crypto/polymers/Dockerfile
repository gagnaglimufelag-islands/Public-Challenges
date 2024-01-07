FROM python:2-alpine

RUN apk add --no-cache socat
ENV PYTHONUNBUFFERED=1

COPY server.py /src/
COPY companySecrets.py /src/
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
