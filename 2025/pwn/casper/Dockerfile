FROM ubuntu:24.04 AS isolate

RUN apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install


FROM ubuntu:24.04 AS bin

RUN apt-get update && apt-get install -y gcc gcc-multilib make

WORKDIR /build
COPY src.c Makefile /build/
RUN make


FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    libc6-i386 \
    libc-dev libcap-dev musl-dev socat \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /src
COPY --from=bin /build/casper /src
COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

CMD echo $FLAG > /src/flag.txt && \
    isolate -b 0 --init && \
    isolate -b 0 --processes=40 \
                 --share-net \
                 --dir=/lib32 \
                 --dir=/src \
                 -c /src \
                 --env=PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin \
                 --run -- /usr/bin/socat tcp-listen:32000,reuseaddr,fork exec:./casper && \
    isolate -b 0 --cleanup

EXPOSE 32000
