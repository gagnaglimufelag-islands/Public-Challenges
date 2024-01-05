# Elaris-final

we are given a *PNG* file which has a *ZIP* file embedded in it, after using `binwalk` to extract the file from the image, we have to supply a password to decompress the zip file. After brute-forcing the password it's revealed that the password is `Crystal` with that password
we can unzip and get two files *Key.txt* and *Treasure.jpg*. The contents of *Key.txt* is written using the esoteric programming language  [COW](https://esolangs.org/wiki/COW) after decoding that we are left with a key and a base64 string which decodes to `steghide`.
Now we have the neccessary information to extract the flag from the image file in the zip file, by using steghide with the key given in the *Key.txt* file we can extract the *flag.txt* file. Looking at the contents of *flag.txt* we have multiple thumbs up and thumbs down
emojis, this hints towards it being binary. Writing a python script to replace the thumbs with 1's and 0's we can decode the binary string and get our final flag.


## Introducing Binwalk

When analyzing the given *PNG* file the first few things to look out for is hidden text in the image, the color plane, image size and also it's contents. We can have a look in a hexeditor to examine the contents but there is a very well-known and a handy tool that does much of the work for us called `binwalk`

```
(virtenv) snow@security:~$ binwalk secrets.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
594219        0x9112B         Zip archive data, encrypted at least v2.0 to extract, compressed size: 1442, uncompressed size: 33328, name: Key.txt
595742        0x9171E         Zip archive data, encrypted at least v2.0 to extract, compressed size: 121053, uncompressed size: 121178, name: Treasure.jpg

```

Binwalk detects other files embedded inside our original image file. Binwalk parses the contents of our image file and looks for so-called [Magic-bytes](https://en.wikipedia.org/wiki/List_of_file_signatures) if there is a match for some of these signatures we might have some other files inside our file.
We also see that it's a *ZIP* file containing two files **Key.txt** and **Treasure.jpg**. From here we can utilize the power of binwalk to extract this file out of our image file

```
(virtenv) snow@security:~$ binwalk -e secrets.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 512, 8-bit/color RGBA, non-interlaced
594219        0x9112B         Zip archive data, encrypted at least v2.0 to extract, compressed size: 1442, uncompressed size: 33328, name: Key.txt
595742        0x9171E         Zip archive data, encrypted at least v2.0 to extract, compressed size: 121053, uncompressed size: 121178, name: Treasure.jpg
717040        0xAF0F0         End of Zip archive, footer length: 22

```

Simply running this command above we are left with a new directory `_secrets.png.extracted` moving into this directory we are present with three files but the two most important files are empty, why is that?

```
(virtenv) snow@security:~$ file *
9112B.zip:    Zip archive data, at least v2.0 to extract, compression method=deflate
Key.txt:      empty
Treasure.jpg: empty
```

That's because if we read closely the binwalk output we can see that the zip file is password protected (encrypted), binwalk didn't extract the contents because it doesn't know the password and neither do we


## Introducing fcrackzip

When we encounter a *ZIP* file which is password protected and we don't have a clue about the password combination we grab our handy *rockyou.txt* wordlist and start cracking using `fcrackzip`

```
(virtenv) snow@security:~$ fcrackzip -D -u -p ../rockyou.txt 9112B.zip 


PASSWORD FOUND!!!!: pw == Crystal

```


Now that we have the password to the *ZIP* file we can try to unzip the contents of the file

```
(virtenv) snow@security:~$ unzip -P Crystal 9112B.zip 
Archive:  9112B.zip
replace Key.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: A
  inflating: Key.txt                 
  inflating: Treasure.jpg 
           
(virtenv) snow@security:~$ file *
9112B.zip:    Zip archive data, at least v2.0 to extract, compression method=deflate
Key.txt:      User-mode Linux COW file, version 1867468143, backing file OMMMMMMmoOMMMMOOMOomOoMoOmoOmoomOo
Treasure.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 512x512, components 3
```

Awesome, now we can move on to analyzing the two new files


## The Esoteric Programming Language - COW

By the name of the file **Key.txt** we can assume that there is something hidden in the image file but we are not sure what and how yet so let's examine the text file. Looking at the output of the *file* command
we see a very interesting format called `COW`, if we search this format up online we get that it is an esoteric programming language called [COW](https://esolangs.org/wiki/COW) which functions by knowing multiple variations of the string "moo".
Now with this in mind let's decode this and see what's behind it, we can use any of the online interpreters such as [This one](https://www.cachesleuth.com/cow.html)

```
In the realm of digital mysteries, the intrepid adventurer wielded the obtained key with c3RlZ2hpZGU=, skillfully unlocking the arcane secrets once hidden within the depths of an enigmatic file, revealing a cryptic message awaiting decipherment.
Key: Veiled-illusion-conceals-truth
```

Here is our result, if we look closely there is a base64 encoded string in the text `c3RlZ2hpZGU=` when we decode it we get `steghide`. This tells us that the key can be used with a tool called `steghide` to extract hidden data from the image.


## Introducing steghide

[steghide](https://steghide.sourceforge.net/) is a very well-known steganography tool which is capable of embedding and extracting data from various image and audio files. Let's use it to extract data from our image file

```
(virtenv) snow@security:~$ steghide extract -sf Treasure.jpg 
Enter passphrase: 
wrote extracted data to "flag.txt".
```

Great, now we have our flag file and we can move onto getting our flag


## Getting The Flag

When we open up our **flag.txt** file we are present with a bunch of thumbs up and thumbs down emojis, this is not a flag? Well if we think outside the box
And stare at it for a bit we can see that we have a very obvious pattern thumbs up can be interpreted as `1` and thumbs down can be interpreted as `0` then we have `binary`
Let's swap those thumbs with 1's and 0's and decode the binary string

```python
#!/usr/bin/env python3

with open("flag.txt", "r") as f:
    binary = f.read()

binary_string = ''.join(['1' if x == '👍' else '0' for x in binary])
chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
flag = ''.join([chr(int(chunk, 2)) for chunk in chunks])
print(flag)
```

With this script we get our flag 
