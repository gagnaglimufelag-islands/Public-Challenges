FROM ubuntu:20.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y \
    python3-pip \
    wget \
    fuse \
    libfuse2 \
    checkinstall \
    libwebp-dev \
    libopenjp2-7-dev \
    librsvg2-dev \
    libde265-dev \
    libheif-dev
RUN pip3 install -U flask gunicorn

COPY src /src
WORKDIR /src
RUN echo $FLAG > ./flag.txt
RUN mkdir uploads

RUN wget --output-document convert https://github.com/ImageMagick/ImageMagick/releases/download/7.1.0-38/ImageMagick--gcc-x86_64.AppImage
RUN chmod a+x convert

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD echo $FLAG > ./flag.txt && gunicorn -b 0.0.0.0:5000 app:app
