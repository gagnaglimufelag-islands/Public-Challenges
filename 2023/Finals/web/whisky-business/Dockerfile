FROM debian:bullseye-slim as go-builder

RUN apt-get update && apt-get install -y wget git

WORKDIR /usr/local
RUN wget https://go.dev/dl/go1.20.4.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.20.4.linux-amd64.tar.gz
ENV PATH="$PATH:/usr/local/go/bin"
COPY backend /src

WORKDIR /src
RUN git config --global user.name "Jack Daniels" && git config --global user.email "jack@danie.ls"
RUN git init . && git add . && git commit -m "gg{using_git_like_the_c00l_kidz}"
RUN go build .

FROM nginx

RUN sed -i 's/$remote_addr/$http_x_forwarded_for/' /etc/nginx/nginx.conf

RUN apt-get update && apt-get install -y wget lsb-release gnupg
WORKDIR /tmp
RUN wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
RUN yes 4 | dpkg -i mysql-apt-config*
ENV MYSQL_ROOT_PASSWORD=e32nmdlk200pxpefalcpgderdkzcnv
ENV DEBIAN_FRONTEND=noninteractive
RUN { \
		echo mysql-community-server mysql-community-server/data-dir select ''; \
		echo mysql-community-server mysql-community-server/root-pass password 'my-secret-pw'; \
		echo mysql-community-server mysql-community-server/re-root-pass password 'my-secret-pw'; \
		echo mysql-community-server mysql-community-server/remove-test-db select false; \
	} | debconf-set-selections
RUN apt-get update && apt-get install -y mysql-server

COPY --from=go-builder /src/timeclock /src/timeclock
COPY --from=go-builder /src/config.json /src/config.json

COPY 0-start-mysqld.sh /docker-entrypoint.d/
COPY 1-init-db.sh /docker-entrypoint.d/
COPY 2-run-go.sh /docker-entrypoint.d/

COPY default.conf /etc/nginx/conf.d/
COPY frontend /usr/share/nginx/html
COPY --from=go-builder /src/.git /usr/share/nginx/html/.git
