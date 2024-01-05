FROM python:3.9

WORKDIR /src

COPY ./api/ .
RUN pip3 install -U flask gunicorn

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]
