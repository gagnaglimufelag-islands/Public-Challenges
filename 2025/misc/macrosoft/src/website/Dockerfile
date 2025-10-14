FROM nginx
RUN sed -i 's/$remote_addr/$http_x_forwarded_for/' /etc/nginx/nginx.conf
COPY src /usr/share/nginx/html
