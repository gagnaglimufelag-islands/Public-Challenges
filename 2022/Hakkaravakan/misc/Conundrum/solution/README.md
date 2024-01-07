# Conundrum

We are given a simple `.JPG` and  a `.ZIP` The image file looks very standard but if we look at the size of the image we can see that it's surprisingly big. If we use some common tools to find hidden data on the image file e.g `steghide` when we try to extract the file from the image we are asked for a password, we can make use of the challenge description where it says if the image has any deeper meaning. When we use the number given in the image **1987** we successfully extract the text file and can view it's contents, from there we get a password to unzip the `.ZIP` file where we end up unzipping a `.PNG` which when we try to open up in an image viewer fails. If we take a look at the header of the image file we can very quickly see that the magic bytes are missing for the `.PNG` file format, upon reconstructing the image header we should have a valid `.PNG` image that outputs the flag

## Getting flag.png

```sh
┌──(kali㉿kali)-[~/chal/conundrum]
└─$ ls
meme.jpg  zippy.zip
                                                                                                                                                                         
┌──(kali㉿kali)-[~/chal/conundrum]
└─$ steghide extract -sf meme.jpg
Enter passphrase: 
wrote extracted data to "password.txt".
                                                                                                                                                                         
┌──(kali㉿kali)-[~/chal/conundrum]
└─$ cat password.txt 
The zip file password is: NeverGonnaGiveYouUP
                                                                                                                                                                         
┌──(kali㉿kali)-[~/chal/conundrum]
└─$ unzip zippy.zip 
Archive:  zippy.zip
[zippy.zip] flag.png password: 
  inflating: flag.png  
```


## Reconstructing flag.png

```sh
─(kali㉿kali)-[~/chal/conundrum]
└─$ xxd flag.png | head
00000000: 0000 0000 0000 0000 0000 000d 4948 4452  ............IHDR
00000010: 0000 0c29 0000 0098 0806 0000 0073 ec52  ...).........s.R
00000020: e100 0000 0467 414d 4100 00b1 8f0b fc61  .....gAMA......a
00000030: 0500 0000 0662 4b47 4400 ff00 ff00 ffa0  .....bKGD.......
00000040: bda7 9300 0000 0970 4859 7300 000b 1300  .......pHYs.....
00000050: 000b 1301 009a 9c18 0000 0007 7449 4d45  ............tIME
00000060: 07e6 0a1a 0023 24fb 776e d500 0020 0049  .....#$.wn... .I
00000070: 4441 5478 daec bd79 9425 d95d dff9 89e5  DATx...y.%.]....
00000080: 45bc 25b7 5abb 4bad ea6e f526 0b21 836c  E.%.Z.K..n.&.!.l
00000090: 4018 0964 8419 cf80 c720 6430 6338 c320  @..d..... d0c8. 
```

![Reconstruct](pic/hex.png)
*Re-adding Magic Bytes*

```sh
┌──(kali㉿kali)-[~/chal/conundrum]                                                                                                                                       
└─$ xxd flag.png | head                                                                                                                                                  
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR                                                                                                      
00000010: 0000 0c29 0000 0098 0806 0000 0073 ec52  ...).........s.R                                                                                                      
00000020: e100 0000 0467 414d 4100 00b1 8f0b fc61  .....gAMA......a                                                                                                      
00000030: 0500 0000 0662 4b47 4400 ff00 ff00 ffa0  .....bKGD.......                                                                                                      
00000040: bda7 9300 0000 0970 4859 7300 000b 1300  .......pHYs.....                                                                                                      
00000050: 000b 1301 009a 9c18 0000 0007 7449 4d45  ............tIME                                                                                                      
00000060: 07e6 0a1a 0023 24fb 776e d500 0020 0049  .....#$.wn... .I                                                                                                      
00000070: 4441 5478 daec bd79 9425 d95d dff9 89e5  DATx...y.%.]....                                                                                                      
00000080: 45bc 25b7 5abb 4bad ea6e f526 0b21 836c  E.%.Z.K..n.&.!.l                                                                                                      
00000090: 4018 0964 8419 cf80 c720 6430 6338 c320  @..d..... d0c8. 
```
