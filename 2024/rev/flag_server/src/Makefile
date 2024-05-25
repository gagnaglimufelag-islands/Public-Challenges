GO := $(shell which go)
BINARY := $(shell basename "$(PWD)")
BUILDDIR := $(shell pwd)/bin

all: clean fmt lint vet test build

.PHONY: build
build:
	@echo "[+] $@"
	@$(GO) build -o $(BUILDDIR)/server ./cmd/server/main.go

.PHONY: fmt
fmt:
	@echo "[+] $@"
	@gofmt -s -l .
	@golangci-lint run --fix ./...

.PHONY: lint
lint:
	@echo "[+] $@"
	@golangci-lint run

.PHONY: vet
vet:
	@echo "[+] $@"
	@$(GO) vet ./...

.PHONY: test
test:
	@echo "[+] $@"
	@$(GO) test ./...

.PHONY: clean
clean:
	@echo "[+] $@"
	@$(RM) -r $(BUILDDIR)/server
