FROM hdgigante/python-opencv:4.7.0-alpine

RUN apk add --no-cache socat
RUN pip install Pillow
ENV PYTHONUNBUFFERED=1

COPY server.py /src/
COPY isthisloss.png /src/
WORKDIR /src

CMD socat tcp-listen:32000,reuseaddr,fork exec:'/usr/local/bin/python server.py'
