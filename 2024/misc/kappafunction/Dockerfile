FROM golang:1.22

COPY src /src
WORKDIR /src

RUN go install .
RUN go build .

ENV PORT 80
ENV GIN_MODE release
ENV cookie_secret AkSNCUW89jkg6rPfccfIGBZKnIDSQgsK
CMD ["go","run","web.go"]
