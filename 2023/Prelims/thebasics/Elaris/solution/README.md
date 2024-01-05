# Elaris

We have a `PNG` file which hides data using LSB steganography. To extract the flag from the image we can use a tool called [zsteg](https://github.com/zed-0xff/zsteg)



```
root@security:~# zsteg Treasure.png
b1,g,msb,xy         .. text: "+:|AE&%7"
b1,b,lsb,xy         .. text: "gg{Find_the_tree_that_whispers_secrets_and_the_island_lies_where_its_roots_converge}"
b1,bgr,lsb,xy       .. text: "7#F}]u>A"
b1,rgba,lsb,xy      .. file: PGP Secret Sub-key -
b2,g,msb,xy         .. text: ";S%v1<Yc"
b2,b,lsb,xy         .. text: ["U" repeated 9 times]
b2,rgba,lsb,xy      .. text: "37WWK?;;K?"
b3,g,lsb,xy         .. file: OpenPGP Secret Key
b3,bgr,msb,xy       .. file: OpenPGP Public Key
b4,r,lsb,xy         .. text: "=@V=qu>&"
b4,r,msb,xy         .. text: "U33333333"
b4,g,lsb,xy         .. text: "trgfffffff"
```
