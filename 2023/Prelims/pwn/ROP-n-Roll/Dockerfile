FROM ubuntu:20.04 AS isolate

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install


FROM ubuntu:20.04 AS bin

RUN apt-get update && apt-get install -y gcc gcc-multilib make

WORKDIR /build
COPY src/ /build
RUN ./build.sh


FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    libc6-i386 \
    libc-dev libcap-dev musl-dev socat \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /src
COPY --from=bin /build/chal /usr/local/bin/chal
COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

RUN mkdir /inner-etc && \
    echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf && \
    echo "root:x:0:0::/root:/bin/bash" > /inner-etc/passwd

CMD echo $FLAG > /src/flag.txt && \
    isolate -b 0 --init && \
    isolate -b 0 \ 
            --processes \
            --share-net \
            --dir=/lib32 \
            --dir=/etc=/inner-etc \
            --dir=/src \
            -c /src \
            --env=PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin \
            --run -- /usr/bin/socat tcp-listen:32000,reuseaddr,fork exec:/usr/local/bin/chal && \
    isolate -b 0 --cleanup

EXPOSE 32000

