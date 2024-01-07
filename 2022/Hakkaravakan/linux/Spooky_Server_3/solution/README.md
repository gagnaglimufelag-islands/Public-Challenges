# Spooky Server 3
```bash
find / -user ghost -type f  -printf "%T@ %p\n" 2> /dev/null | grep -v "/\." | sort -n | cut -f 2 -d " " | xargs cat
```
