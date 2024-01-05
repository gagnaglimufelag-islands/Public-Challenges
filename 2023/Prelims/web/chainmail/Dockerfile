FROM debian:bullseye-slim as isolate

RUN apt-get update && apt-get -y install git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install


FROM mcr.microsoft.com/dotnet/sdk:7.0-bullseye-slim as builder

COPY App /src/
WORKDIR /src
RUN dotnet publish -o out


FROM mcr.microsoft.com/dotnet/aspnet:7.0-bullseye-slim

COPY --from=builder /src/out /src/

RUN apt-get update && apt-get install -y libc-dev libcap-dev curl strace

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

RUN mkdir -p /inner-etc /secrets/top
RUN echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf

WORKDIR /src

CMD cp -r /etc/ca-certificates/ /inner-etc && \
    cp -r /etc/ssl/ /inner-etc && \
    echo $FLAG > /secrets/top/flag.txt &&\
    isolate -b 0 --init && \
    isolate -b 0 \
            --processes \
            --open-files=0 \
            --share-net \
            -e --env=FLAG= --env=ASPNETCORE_URLS="http://+:5000" --env=ASPNETCORE_ENVIRONMENT=Development \
            --dir=/etc=/inner-etc --dir=/var --dir=/secrets --dir=/src \
            -c /src --run -- ./App && \
    #isolate -b 0 \
    #        --processes \
    #        --open-files=0 \
    #        --share-net \
    #        -e --env=FLAG= --env=ASPNETCORE_URLS="http://+:5000" --env=ASPNETCORE_ENVIRONMENT=Development \
    #        --dir=/etc=/inner-etc --dir=/var --dir=/secrets --dir=/src \
    #        --tty-hack \
    #        -c /src --run -- /bin/bash && \
    isolate -b 0 --cleanup

