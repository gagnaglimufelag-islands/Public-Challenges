FROM debian:bullseye-slim as isolate

RUN apt-get update && apt-get -y install git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install


FROM mcr.microsoft.com/dotnet/sdk:7.0-bullseye-slim as builder

COPY App /src/
WORKDIR /src

RUN dotnet publish -c Release -o out
RUN cp -r Db out


FROM mcr.microsoft.com/dotnet/aspnet:7.0-bullseye-slim

COPY --from=builder /src/out /src/

WORKDIR /src

RUN apt-get update && apt-get install -y sqlite3 libc-dev libcap-dev curl strace

RUN sqlite3 Db/app.db "DELETE FROM Postcodes WHERE Hidden=1"

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

RUN mkdir /inner-etc
RUN echo "nameserver 8.8.8.8" > /inner-etc/resolv.conf
RUN chmod 777 Db

CMD cp -r /etc/ca-certificates/ /inner-etc && \
    cp -r /etc/ssl/ /inner-etc && \
    sqlite3 Db/app.db "INSERT INTO Postcodes (Id, Name, Hidden) VALUES (1337, '$FLAG', 1)" && \
    isolate -b 0 --init && \
    isolate -b 0 \
            --processes \
            --open-files=0 \
            --share-net \
            -e --env=FLAG= --env=ASPNETCORE_URLS="http://+:5000" --env=ASPNETCORE_ENVIRONMENT=Development \
            --dir=/etc=/inner-etc --dir=/var --dir=/src:rw \
            -c /src --run -- ./App && \
    isolate -b 0 --cleanup

