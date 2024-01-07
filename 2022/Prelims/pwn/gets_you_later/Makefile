CC := gcc
CFLAGS = -O0 -fno-stack-protector -no-pie -D_FORTIFY_SOURCE=0
BINARY := $(shell basename "$(PWD)")

build:
	@echo "[+] $@"
	@$(CC) $(CFLAGS) main.c -o $(BINARY)

ubuntu-build:
	sudo docker build -f Dockerfile.bin -t $(BINARY)-builder .
	sudo docker run --rm $(BINARY)-builder > $(BINARY)
	chmod +x $(BINARY)
	sudo docker image rm $(BINARY)-builder
