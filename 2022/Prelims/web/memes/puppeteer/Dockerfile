FROM buildkite/puppeteer

RUN adduser --disabled-password \
        --gecos '' \
        --home /home/usr \
        usr
COPY example.js /data/example.js

ENV ADMIN_PASSWORD OMmHQw9S0hSTVdvQ9WzZdW148

CMD node /data/example.js
