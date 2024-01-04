# Bubettuber thuban ubEllubiptubic cuburvube
The description is semi-readable gibberish followed by a hint that tells us that the flag is readable and is compose of english words.

We are given a file `tubext.txt` and it contains more of this semi-readable gibberish. When we analyse this file we quickly realize that for each vowel a `ub` string is prepended to the vowel.

This means we can decode the gibberish with the following script:

```python
import sys

VOWELS = ['A', 'Á', 'E', 'É', 'I', 'Í', 'O', 'Ó', 'U', 'Ú', 'Y', 'Ý', 'Æ', 'Ö']
KEY = "ub"

s = ""
with open("./tubext.txt", "r") as f:
    s = f.read()

i = 0
while i < len(s):
    if i < len(s) - 2 and s[i].lower() == "u" and s[i+1].lower() == "b" and s[i+2].upper() in VOWELS:
        sys.stdout.write(s[i+2])
        i += 2
    else:
        sys.stdout.write(s[i])
    i += 1
```

Now we can grep for the flagformat like so `grep gg{` and we get the flag
