FROM python:3.10-alpine

RUN pip install -U flask

COPY src /src
WORKDIR /src

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD flask run
