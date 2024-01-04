# Emojifier
This challenge is vulnerable to CVE-2022-44268 a arbitrary file read in ImageMagick

Steps to solve:
* Upload image
* Download resized image
* Read metadata of image
* Google ImageMagick 7.1.0 Vulnerability
* Change value of Profile tExt chunk of image to flag.txt
* Upload file with updated value 
* Download resized image
* Run `exiftool -b downloaded_image.png`
* Find hex string and decode

