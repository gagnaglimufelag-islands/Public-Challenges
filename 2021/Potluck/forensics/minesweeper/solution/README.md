# Minesweeper
Find profile.

volatility -f memdump.raw imageinfo

Look at internet explorer history.

volatility -f memdump.raw --profile=WinXPSP3x86 iehistory

See that they accessed a local website.
Find where in memory the website is located.

volatility -f memdump.raw --profile=WinXPSP3x86 filescan | grep -i index.html

Dump the file.

volatility -f memdump.raw --profile=WinXPSP3x86 dumpfiles -Q 0x000000000222d3d8 -D .

Open the site and get the flag.
