FROM sagemath/sagemath

USER root

RUN apt-get update && apt-get install -y socat
COPY server.py /src/server.py
COPY flag.txt /src/flag.txt
RUN chown -R sage:sage /src

USER sage

WORKDIR /src
ENV PYTHONUNBUFFERED=1
CMD ["socat", "tcp-listen:32000,reuseaddr,fork exec:'/usr/bin/sage server.py'"]
