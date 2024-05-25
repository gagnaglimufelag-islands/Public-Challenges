FROM ubuntu:23.10 AS isolate

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install



FROM ubuntu:23.10

RUN apt-get update && apt-get install -y \
    libc6-i386 \
    libc-dev \
    libcap-dev \
    musl-dev \
    socat \
    python3 \
    && rm -rf /var/lib/apt/lists/*

COPY src /src
WORKDIR /src

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

RUN mkdir /inner-etc && \
    echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf && \
    echo "root:x:0:0::/root:/bin/bash" > /inner-etc/passwd

CMD isolate -b 0 --init && \
    isolate -b 0 --processes=40 \
    --share-net \
    --dir=/lib32 \
    --dir=/etc=/inner-etc \
    --dir=/src/ \
    -c /src/ \
    --env=PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin \
    --run -- /usr/bin/socat tcp-listen:32000,reuseaddr,fork exec:'python3 /src/main.py' && \
    isolate -b 0 --cleanup

EXPOSE 32000
