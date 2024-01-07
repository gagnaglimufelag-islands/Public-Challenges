FROM nginx
RUN sed -i 's/$remote_addr/$http_x_forwarded_for/' /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/
COPY src /usr/share/nginx/html
COPY default.conf /usr/share/nginx/html
COPY setup-flag.sh /docker-entrypoint.d/
