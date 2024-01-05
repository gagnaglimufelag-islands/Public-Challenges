FROM ubuntu:rolling

WORKDIR /app
COPY . .

RUN apt-get update \
	&& apt-get install -y clang \
	&& rm -rf /var/lib/apt/lists/*

CMD ["./make.sh"]
