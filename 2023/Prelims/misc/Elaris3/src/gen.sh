#!/bin/bash


# use steghide to embed flag.txt to image
steghide embed -cf cover/embed.jpg -ef cover/flag.txt -sf Treasure.jpg -p "Veiled-illusion-conceals-truth"

# Create zip-file with password 'Crystal' containing key.txt & Treasure.jpg
zip --password "Crystal" deception.zip Key.txt Treasure.jpg


# Create PNG image with zip file embedded
cat cover/embed2.png deception.zip > secrets.png

# Remove unused stuff
rm Treasure.jpg
rm deception.zip

