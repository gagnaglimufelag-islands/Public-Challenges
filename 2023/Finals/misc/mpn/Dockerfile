FROM debian:bullseye-slim as isolate

RUN apt-get update && apt-get -y install git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install

FROM python:3.11-slim-bullseye

RUN pip install -U flask
RUN apt-get update && apt-get install -y libc-dev libcap-dev npm

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

COPY src /src
WORKDIR /src
RUN mkdir /inner-etc

CMD cp /etc/resolv.conf /inner-etc && \
    cp -r /etc/ca-certificates/ /inner-etc && \
    cp -r /etc/ssl/ /inner-etc && \
    isolate -b 0 --init && \
    isolate -b 0 \
            --processes \
            --open-files=0 \
            --share-net \
            --env=LD_LIBRARY_PATH=/usr/local/lib \
            --env=HOME=/tmp \
            --env=FLAG \
            --dir=/etc=/inner-etc \
            --dir=/src \
            -c /src \
            --run -- /usr/local/bin/flask run --host=0.0.0.0 && \
    isolate -b 0 --cleanup

