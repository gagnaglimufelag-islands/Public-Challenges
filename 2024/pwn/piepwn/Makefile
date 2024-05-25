all: docker

.PHONY: docker
docker:
	@echo "[+] $@"
	@docker build -t piepwn .
	@docker run -it --privileged --rm -p 32000:32000 --name piepwn piepwn
