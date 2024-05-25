FROM buildkite/puppeteer

RUN adduser --disabled-password \
        --gecos '' \
        --home /home/usr \
        usr
COPY example.js /data/example.js

CMD node /data/example.js
