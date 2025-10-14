FROM alpine:latest AS builder

RUN apk update && \
    apk add build-base

WORKDIR /src
COPY src/radio_net_module.c radio_net_module.c
COPY Makefile .

RUN make

FROM scratch AS gib_binary
COPY --from=builder /src/radio_net_module.cgi /radio_net_module.cgi

FROM busybox:latest

WORKDIR /var/www
RUN mkdir -p /var/www/cgi-bin

COPY --from=builder /src/radio_net_module.cgi /var/www/cgi-bin/radio_net_module.cgi
RUN chmod +x /var/www/cgi-bin/radio_net_module.cgi

COPY flag.txt /flag.txt
RUN chown www-data:www-data /flag.txt && chmod 444 /flag.txt

RUN mkdir -p /var/log && \
    echo "$(date) - System boot sequence initiated." > /var/log/device.log && \
    echo "$(date) - Network interface eth0 configured." >> /var/log/device.log && \
    echo "$(date) - Services started successfully." >> /var/log/device.log && \
    echo "$(date) - User 'admin' logged in from 192.168.1.100." >> /var/log/device.log && \
    echo "$(date) - Warning: Low disk space on /data." >> /var/log/device.log && \
    echo "$(date) - System health check: OK." >> /var/log/device.log && \
    echo "$(date) - Scheduled backup started." >> /var/log/device.log && \
    echo "$(date) - Scheduled backup completed." >> /var/log/device.log && \
    echo "$(date) - Firmware update check: No new updates." >> /var/log/device.log && \
    echo "$(date) - User 'guest' failed login attempt from 10.0.0.5." >> /var/log/device.log && \
    echo "$(date) - System shutdown initiated by 'admin'." >> /var/log/device.log && \
    chown www-data:www-data /var/log/device.log && chmod 644 /var/log/device.log

RUN chown -R www-data:www-data /var/www
RUN chmod -R 755 /var/www/cgi-bin

EXPOSE 80
CMD ["busybox", "httpd", "-f", "-v", "-p", "0.0.0.0:80", "-h", "/var/www"]
