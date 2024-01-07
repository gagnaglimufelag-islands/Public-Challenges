FROM ubuntu:latest

COPY ./sudo /build
RUN apt-get update && \
    apt-get -y install gcc libncurses-dev make git

WORKDIR /build
RUN ./configure
RUN make
RUN make install

WORKDIR /

RUN rm -rfv /build

RUN yes | unminimize
RUN apt-get update && apt-get -y install man less

RUN adduser --disabled-password \
            --gecos '' \
            --home /home/martin \
            martin

RUN adduser --disabled-password \
            --gecos '' \
            --home /home/jon \
            jon

# # Initial flag: Message of the day
COPY motd /etc/
RUN cat /etc/motd >> /home/martin/.bashrc

# First flag: dotfile
COPY --chown=martin:martin flag1.txt /home/martin/
RUN mv /home/martin/flag1.txt /home/martin/.flag1.txt

# Second flag "hidden" by a sed command run by jon
COPY --chown=jon:jon zsh_history /home/jon/.zsh_history
RUN mkdir /etc/wat/
COPY --chown=jon:jon flag2.txt /etc/wat/inconspicuous
RUN sed -i -e 's/gg{/hidden[/' -e 's/}/]/' -e 's/4/A/' /etc/wat/inconspicuous

# Third flag: "ransomware"
COPY --chown=martin:martin flag3/ransom /home/martin/shredder

# Fifth flag: in jon's home directory
RUN mkdir /home/jon/flags
COPY flag4.txt /home/jon/flags/
RUN chown -R jon:jon /home/jon/flags
RUN chmod 600 /home/jon/flags/flag4.txt

# Fifth flag: in root's home directory
RUN mkdir /root/flags
RUN chmod +xr /root/
COPY flag5.txt /root/flags/
RUN chmod 600 /root/flags/flag5.txt

RUN echo 'ALL ALL=(ALL, !root) NOPASSWD: /usr/bin/cat' >> /etc/sudoers
RUN chmod a+r /etc/sudoers

USER martin

WORKDIR /home/martin

ENTRYPOINT ["/bin/bash"]
