FROM python:3.9

RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y dnsutils --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY ./src .
COPY flag.txt /src/
RUN pip3 install -U flask gunicorn python-dotenv

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]
