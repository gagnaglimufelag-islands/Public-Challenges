sudo docker build -f Dockerfile.binary-build -t binary-builder .
sudo docker run --mount type=bind,source=$(pwd)/src,target=/build binary-builder
