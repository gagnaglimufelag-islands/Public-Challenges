GO := $(shell which go)
BINARY := $(shell basename "$(PWD)")
BUILDDIR := $(shell pwd)/bin

all: docker

.PHONY: docker
docker:
	@echo "[+] $@"
	@docker build -t flag_server .
	@docker stop flag_server
	@docker run -it -d --rm -p 32000:32000 --name flag_server flag_server
	@docker cp flag_server:/usr/bin/server ./src/bin/server-linux
