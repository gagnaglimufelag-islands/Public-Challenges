FROM alpine:3.11 AS isolate

RUN apk add git make gcc libc-dev libcap-dev
RUN git clone https://github.com/gagnaglimufelag-islands/isolate.git
WORKDIR /isolate
RUN make -f Makefile.nodocs && make -f Makefile.nodocs install


FROM python:3.11-alpine

RUN pip install -U flask gunicorn pycryptodome
RUN apk add libc-dev libcap-dev

COPY --from=isolate /usr/local/bin/isolate /usr/local/bin/isolate
COPY --from=isolate /usr/local/etc/isolate /usr/local/etc/isolate
COPY --from=isolate /var/local/lib/isolate /var/local/lib/isolate

COPY app.py app.py
COPY evaluate.py evaluate.py
COPY templates templates

CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]
