build:
	gcc -o runner runner.c
handout:
	gcc -o medusa medusa.c
run:
	cat meta.yml | yq -r .flags | base64 -w 0 | base32 -w 0 | base64 -w 0 | base32 -w 0 > fakehome/.secrets/flag 
	gcc -o runner runner.c
	export HOME="./fakehome"
	./runner
