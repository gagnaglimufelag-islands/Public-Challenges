FROM ubuntu:latest

RUN apt-get update && \
    apt-get -y install gcc libncurses-dev make git python3

WORKDIR /

RUN yes | unminimize
RUN apt-get update && apt-get -y install man less

RUN adduser --disabled-password \
            --gecos '' \
            --home /home/dalle \
            dalle

RUN adduser --disabled-password \
            --gecos '' \
            --home /home/gpt \
            gpt

COPY motd /etc/
RUN cat /etc/motd >> /home/dalle/.bashrc

# Initial flag: "hidden" file
COPY --chown=dalle:dalle flag0.txt /home/dalle/.flag0.txt

# First flag: File name is dash which will be annoying for cat
COPY --chown=dalle:dalle flag1.txt "/home/dalle/-"

# Second flag: diretory named space
RUN mkdir "/home/dalle/ " && chown dalle:dalle "/home/dalle/ "
COPY --chown=dalle:dalle flag2.txt /home/dalle/
RUN mv /home/dalle/flag2.txt "/home/dalle/ /flag2.txt"

# Third flag: hidden flag in many directories
COPY mkflag3.sh /home/dalle/
WORKDIR /home/dalle/
RUN ./mkflag3.sh
RUN rm mkflag3.sh

# Third flag: Borken Hijack cronjob of the user gpt
COPY --chown=gpt:gpt flag4.txt /home/gpt/
COPY --chown=gpt:gpt train.sh /home/gpt/
RUN chmod 777 /home/gpt/train.sh
RUN chmod 711 /home/gpt

# Third flag: Borken Hijack cronjob of the user gpt
COPY --chown=gpt:gpt flag4.5.txt /home/gpt/s3crtstuff/flag45-nowW1thextrapadding.txt
RUN chmod 711 /home/gpt/s3crtstuff
RUN chmod 600 /home/gpt/s3crtstuff/flag45-nowW1thextrapadding.txt

COPY personal /root/personal
COPY flag5.txt /root/flag.txt

WORKDIR /home/dalle

RUN apt-get update && apt-get install -y vim sudo cron zip zsh
RUN mkdir --mode=777 /tmp/backup

RUN sed -i "s/alias ls='ls --color=auto'/alias ls='ls --color=auto --quoting-style=literal'/" .bashrc

# Add crontab files to the cron directory
ADD crontab-backup /etc/cron.d/backup
ADD crontab-hijack /etc/cron.d/train

# Give execution rights on the cron jobs
RUN chmod 0644 /etc/cron.d/backup
RUN chmod 0644 /etc/cron.d/train

RUN apt-get install -y locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN echo 'LANG=en_US.UTF-8' >> /etc/environment
RUN echo 'LANGUAGE=en_US:en' >> /etc/environment
RUN echo 'LC_ALL=en_US.UTF-8' >> /etc/environment

ENTRYPOINT echo "127.0.0.1 $(cat /etc/hostname)" >> /etc/hosts && cron & sudo -u dalle /bin/bash
