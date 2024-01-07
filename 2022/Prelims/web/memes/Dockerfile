FROM python:3.9-alpine

RUN pip install -U flask gunicorn

COPY src /src
WORKDIR /src

ENV ADMIN_PASSWORD OMmHQw9S0hSTVdvQ9WzZdW148

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]
