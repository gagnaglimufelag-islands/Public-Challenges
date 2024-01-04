FROM ubuntu:20.04 AS isolate

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install


FROM ubuntu:20.04 AS bin

RUN apt-get update && apt-get install -y gcc gcc-multilib make 

WORKDIR /build
COPY src/main.c /build
COPY src/makefile /build
RUN make


FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    libc6-i386 \
    sudo \
    libc-dev libcap-dev musl-dev socat \
    && rm -rf /var/lib/apt/lists/* 

RUN mkdir /src
COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate
COPY --from=bin /build/chal /src/chal
COPY runner.sh /src

RUN mkdir /inner-etc && \
    echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf && \
    echo "root:x:0:0::/root:/bin/bash" > /inner-etc/passwd

RUN sudo sysctl kernel.randomize_va_space=0

WORKDIR /src

CMD echo $FLAG > /src/flag.txt && socat tcp-listen:32000,reuseaddr,fork exec:./runner.sh


EXPOSE 32000
