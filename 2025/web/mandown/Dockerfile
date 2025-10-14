FROM python:3.9-alpine

RUN pip install -U flask gunicorn

COPY src /src
WORKDIR /src

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1
CMD ["gunicorn", "--access-logfile", "-", "--access-logformat", "%({x-forwarded-for}i)s %(l)s %(u)s %(t)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\"", "-b", "0.0.0.0:5000", "app:app"]
