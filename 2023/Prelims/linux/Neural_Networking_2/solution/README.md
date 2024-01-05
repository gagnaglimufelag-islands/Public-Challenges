## Neural Network 2
When looking at the output of the original `ll` command you will notice a directory with a whitespace for a name.
Now because whitespace is a character which is interpreted in Linux you have to enclose it in quotes, like so:
```bash
dalle@0d5c22beacee:~$ ll " "
total 16
drwxr-xr-x 1 dalle dalle 4096 Apr  1 16:08 ./
drwxr-x--- 1 dalle dalle 4096 Apr  1 16:09 ../
-rw-r--r-- 1 dalle dalle   37 Apr  1 11:37 flag2.txt
```

```bash
cat " /flag2.txt"
```
