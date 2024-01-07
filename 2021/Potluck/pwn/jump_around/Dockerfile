FROM ubuntu:18.04 AS isolate

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git make gcc libc-dev libcap-dev asciidoc
RUN git clone https://github.com/ioi/isolate.git
WORKDIR /isolate
RUN make && make install


FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    libc6-i386 \
    libc-dev libcap-dev musl-dev socat \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /secrets
COPY flag.txt /secrets
COPY jump_around /usr/local/bin

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

RUN mkdir /inner-etc && \
    echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf && \
    echo "root:x:0:0::/root:/bin/bash" > /inner-etc/passwd

CMD isolate -b 0 --init && \
    isolate -b 0 --processes=40 --share-net --dir=/lib32 --dir=/etc=/inner-etc --dir=/secrets -c /secrets --env=PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin --run -- /usr/bin/socat tcp-listen:32000,reuseaddr,fork exec:/usr/local/bin/jump_around && \
    isolate -b 0 --cleanup

EXPOSE 32000

