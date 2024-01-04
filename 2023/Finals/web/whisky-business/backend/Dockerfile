# syntax=docker/dockerfile:1

FROM golang:alpine

WORKDIR /app

# Copy the source from the current directory to the working Directory inside the container
COPY . .
RUN go mod download

# Build the Go app
RUN go build -o /timeclock

EXPOSE 8080

CMD [ "/timeclock" ]