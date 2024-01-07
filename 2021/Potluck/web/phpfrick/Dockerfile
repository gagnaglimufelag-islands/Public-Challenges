FROM debian:buster as isolate

RUN apt-get update
RUN apt-get install --yes git make gcc libc-dev libcap-dev asciidoc
RUN git clone https://github.com/ioi/isolate.git
WORKDIR /isolate
RUN make && make install

FROM php:apache

RUN apt-get update
RUN apt-get install --yes libc-dev libcap-dev
RUN apt-get install --yes --force-yes cron g++ gettext libicu-dev openssl libc-client-dev libkrb5-dev  libxml2-dev libfreetype6-dev libgd-dev libmcrypt-dev bzip2 libbz2-dev libtidy-dev libcurl4-openssl-dev libz-dev libmemcached-dev libxslt-dev

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

COPY src /usr/src/irregular_statements
RUN mkdir /inner-etc

CMD cp /etc/resolv.conf /inner-etc && \
    cp -r /etc/ca-certificates/ /inner-etc &&\
    cp -r /etc/ssl/ /inner-etc &&\
    isolate -b 0 --init && \
    isolate -b 0 --processes --share-net --dir=/etc=/inner-etc --dir=/src=/usr/src/irregular_statements --dir=/tmp -c /src --run -- /usr/local/bin/php -S 0.0.0.0:8000 ./index.php && \
    isolate -b 0 --cleanup
