# Lost file contents
A simple windows memory forensics challenge where the flag is hidden in two places in the notepad process.

The first part of the challenge is to identify the correct process the flag is located in. The name of the challenge and description should give a hint that this is the notepad.exe process.

We unzip the memory dump and start by running volatility on it. Both volatility 2 and 3 should work but I used volatility 2 for the following solution. Steps should be pretty similar for volatility 3.

We start by identifying a potential profile we can use by running imageinfo: `vol.py -f ./memdump.raw imageinfo`

That takes a while but suggests we could use `Win10x64_19041` as our profile. Next we get a list of all running processes at the time the memory dump was taken: `vol.py -f ./memdump.raw --profile=Win10x64_19041 pslist`

There we can see the notepad.exe process has a pid of 5972, we next proceed by dumping that processes memory: `vol.py -f ./memdump.raw --profile=Win10x64_19041 memdump -p 5972 --dump-dir=dump/`

A simple step sould be to start by running the strings command on that dump and grepping for a known part of the flag: `strings 5972.dmp | grep "gg{"`. In this case, it results in the first part of the flag: `gg{a_visual_` rest of the flag is still missing.

I often like to start by changing the filename of our dump from `5972.dmp` to `5972.data`. This allows us to open the dump in a program such as gimp. By setting the image type to RGB Alpha and fiddling with the image width, we can spot a frame buffer which contains our notepad window and the text loaded at the time of the memory dump. There we can see the second part of our flag `and_volatile_challenge}`

![second flag part](src/p1.png "Second flag part")

