FROM ubuntu:latest as ghost

RUN apt-get update && apt-get -y install python3

RUN mkdir /src
COPY gen.py /src
COPY flag3.txt /src
WORKDIR /src

CMD python3 gen.py
