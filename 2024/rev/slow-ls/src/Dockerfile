FROM ubuntu:24.04

RUN mkdir /src
RUN mkdir /build

WORKDIR /src

RUN apt update && apt upgrade -y
RUN apt install g++ build-essential -y

COPY ./main.c /src
COPY ./makefile /src
COPY ./build.sh /src

RUN chmod +x ./build.sh

#RUN make
#RUN cp ./main /build/app

CMD ["/bin/bash", "/src/build.sh"]
