FROM ubuntu:latest

RUN apt-get update && \
    apt-get -y install gcc libncurses-dev make git python3

WORKDIR /

RUN yes | unminimize
RUN apt-get update && apt-get -y install man less

RUN adduser --disabled-password \
            --gecos '' \
            --home /home/skeleton \
            skeleton

RUN adduser --disabled-password \
            --gecos '' \
            --home /home/ghost \
            ghost

COPY motd /etc/
RUN cat /etc/motd >> /home/skeleton/.bashrc

# Initial flag: escape vim to be able to cat flag
COPY --chown=skeleton:skeleton flag0.txt /home/skeleton/flag0.txt

# First flag: tilde directory
RUN mkdir "/home/skeleton/~"
COPY --chown=skeleton:skeleton flag1.txt /home/skeleton/
RUN mv /home/skeleton/flag1.txt "/home/skeleton/~/flag1.txt"

# Second (kind of 1.1) flag: file named empty string
COPY flag2.txt /home/skeleton/
RUN mv /home/skeleton/flag2.txt "/home/skeleton/ "

COPY personal /root/personal
COPY flag4.txt /root/flag.txt

WORKDIR /root
COPY flag3/setup setup

WORKDIR /root/setup
RUN chmod +x run.sh && ./run.sh
WORKDIR /root
RUN rm -r setup


WORKDIR /home/skeleton

RUN apt-get install -y vim sudo cron zip zsh
RUN mkdir --mode=777 /tmp/backup

RUN sed -i "s/alias ls='ls --color=auto'/alias ls='ls --color=auto --quoting-style=literal'/" .bashrc

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/backup
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/backup

RUN apt-get install -y locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN echo 'LANG=en_US.UTF-8' >> /etc/environment
RUN echo 'LANGUAGE=en_US:en' >> /etc/environment
RUN echo 'LC_ALL=en_US.UTF-8' >> /etc/environment

ENTRYPOINT cron & sudo -u skeleton /bin/vim /etc/motd
# ENTRYPOINT cron & /bin/bash
