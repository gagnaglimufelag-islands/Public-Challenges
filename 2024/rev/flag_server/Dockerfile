FROM golang:1.22 AS build

COPY ./src/ /src
WORKDIR /src

RUN make build


FROM ubuntu:23.10

RUN mkdir /server
WORKDIR /server

COPY --from=build /src/bin/server /usr/bin/server
COPY flag.txt /server/flag.txt

CMD ["/usr/bin/server"]

EXPOSE 32000
