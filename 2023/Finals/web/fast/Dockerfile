FROM alpine:3.15 as isolate

RUN apk add git make gcc libc-dev libcap-dev asciidoc
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install

FROM python:3.7.2-alpine

USER root

RUN apk add --no-cache --virtual .build-deps gcc musl-dev memcached libmemcached libmemcached-dev zlib-dev busybox-extras libcap-dev

COPY src /src
WORKDIR /src

RUN pip install -U Flask Flask-Caching cachelib gunicorn
RUN pip install -r requirements.txt

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

RUN mkdir /inner-etc
RUN echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf

# Remove this for zipped version
RUN mkdir /tmp/api
RUN echo '{"id":"number_of_stats_on_this_api","stats":1}' > /tmp/api/stats
# Remove this for zipped version

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
#ENTRYPOINT echo "0.0.0.0 examplestats.com" >> /etc/hosts & cd /tmp && python3 -m http.server 80 & memcached -l 127.0.0.1 -p 11211 -m 1024 -u root & flask run

CMD echo "0.0.0.0 examplestats.com" >> /etc/hosts && \
    cd /tmp && python3 -m http.server 80 & \
    memcached -l 127.0.0.1 -p 11211 -m 1024 -u root & \
    cp /etc/resolv.conf /inner-etc && \
    cp -r /etc/ca-certificates/ /inner-etc && \
    cp -r /etc/ssl/ /inner-etc && \
    echo $FLAG > /src/flag_xHgbAHvBn && \
    isolate -b 0 --init && \
    isolate -b 0 \
            --processes \
            --share-net \
            --dir=/etc=/inner-etc \
            --dir=/src \
            --env=LD_LIBRARY_PATH=/usr/local/lib \
            --env=PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin \
            -c /src \
            --run -- /usr/local/bin/gunicorn -b "0.0.0.0:5000" "app:app" && \
    isolate -b 0 --cleanup
