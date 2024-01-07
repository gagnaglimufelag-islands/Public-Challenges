FROM python:3.10-alpine

RUN pip install -U flask flask-cors gunicorn

COPY src /src
WORKDIR /src

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]
