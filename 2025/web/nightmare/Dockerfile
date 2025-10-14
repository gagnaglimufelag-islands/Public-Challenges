FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    nginx \
    python3 \
    python3-pip \
    vim && \
    rm -rf /var/lib/apt/lists/* && \
    rm -f /var/www/html/index.nginx-debian.html && \
    rm /etc/nginx/sites-enabled/default

RUN groupadd -r nginx && useradd -r -g nginx nginx

COPY src src
WORKDIR /src
RUN pip3 install -r requirements.txt

COPY nginx.conf /etc/nginx/nginx.conf
COPY win.c /win.c
RUN gcc /win.c -o /win
RUN rm /win.c

RUN sed -i 's/error_log.*/error_log  \/var\/log\/nginx\/error.log  info;/' /etc/nginx/nginx.conf

EXPOSE 80

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
