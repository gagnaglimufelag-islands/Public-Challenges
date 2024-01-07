# esc server 3
```bash
find -type f -newermt 2022-02-22 -not -newermt 2022-02-23 -exec echo -n {} " " \; -exec basename {} \; | sort -V -k 2 -t " " | cut -f 1 -d " " | xargs cat
```
