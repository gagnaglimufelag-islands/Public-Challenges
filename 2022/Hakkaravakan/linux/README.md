
### Install docker


### Create user

```
useradd -m musk
passwd musk
```

### Dockershell

Copy to `/opt/dockershell.sh`

```
#!/bin/sh
sudo docker run --rm -i --memory=50m --cpus=.1 --network none -t linux-server
```

### Sudoers

Run `visudo` and add the following

```
musk    ALL=(ALL:ALL) NOPASSWD: /usr/bin/docker run --rm -i --memory=50m --cpus=.1 --network none -t linux-server
```

### Get rid of MOTD

```
rm /etc/update-motd.d/*
rm /etc/legal
```

Set `PrintLastLog no` in `/etc/ssh/sshd_config`


### Get rid of docker warning about swap limitation

Open `/etc/default/grub`. Edit the `GRUB_CMDLINE_LINUX` line:

```
GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
```


### Audit

Install `auditd`

```
apt install auditd
auditctl -a exit,always -F arch=b32 -S execve
auditctl -a exit,always -F arch=b64 -S execve
```

Copy `monitor.py` to root home and install `requests`

Add a cronjob

```
* * * * * /usr/bin/python3 /root/monitor.py >> /root/monitor.log
```
