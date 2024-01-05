FROM python:slim-bullseye

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  python3-dev \
  uwsgi \
  uwsgi-plugin-python3 \
	texlive \
	texlive-base \
	texlive-latex-recommended \
  && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app
COPY src/ .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flag /flag
COPY readflag.c /readflag.c
RUN gcc /readflag.c -o /readflag
RUN chown root:root /flag     && chmod 400 /flag
RUN chown root:root /readflag && chmod 4755 /readflag

RUN useradd --no-create-home --home-dir /app --shell /bin/false user

ENTRYPOINT ["uwsgi", "--http-socket", ":5000", "--master", "--processes", "8", "--threads", "4", "--uid", "user", "--gid", "user", "--wsgi-file", "/app/app.py"]
