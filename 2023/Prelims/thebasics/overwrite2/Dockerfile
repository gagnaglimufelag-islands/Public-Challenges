FROM ubuntu:22.10 AS isolate

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install


FROM ubuntu:22.10 AS bin

RUN apt-get update && apt-get install -y gcc gcc-multilib make

WORKDIR /build
COPY overwrite.c Makefile /build/
RUN make


FROM ubuntu:22.10

RUN apt-get update && apt-get install -y \
    libc6-i386 \
    libc-dev libcap-dev musl-dev socat \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /secrets
COPY overwrite /usr/local/bin

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

RUN mkdir /inner-etc && \
    echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf && \
    echo "root:x:0:0::/root:/bin/bash" > /inner-etc/passwd

CMD echo $FLAG > /secrets/flag.txt && \
    isolate -b 0 --init && \
    isolate -b 0 --processes=40 --share-net --dir=/lib32 --dir=/etc=/inner-etc --dir=/secrets -c /secrets --env=PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin --run -- /usr/bin/socat tcp-listen:32000,reuseaddr,fork exec:/usr/local/bin/overwrite && \
    isolate -b 0 --cleanup

EXPOSE 32000

