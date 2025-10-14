FROM python:3.12-alpine

COPY src /src
WORKDIR /src
RUN pip install -r requirements.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
CMD ["gunicorn", "--access-logfile", "-", "--access-logformat", "%({x-forwarded-for}i)s %(l)s %(u)s %(t)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\"", "-b", "0.0.0.0:5000", "app:app"]
