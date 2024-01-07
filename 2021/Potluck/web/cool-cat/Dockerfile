FROM python:3.9-alpine

RUN pip install -U flask requests

COPY src /src
WORKDIR /src

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD flask run
