# The Typist
We are given little to no information, just an IP and port to connect to. So we try to connect 
with `nc` and we get nothing back. Let's try sending some data to see what happens. We get back a 
bunch of data starting with `%PDF-1.7`. This is the [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures)
for a PDF file. Lets save the PDF file to disk.

```bash
echo 'hello' | nc domain port > test.pdf
```

Now we can try and figure out what program created this PDF. This can be done using `pdfinfo` or `vim`
or just by reading the strings outputted when we send data to the server.

```bash
❯ pdfinfo test.pdf 
Creator:         Typst 0.13.1
CreationDate:    Sun May 24 17:00:00 2025 GMT
ModDate:         Sun May 24 17:00:00 2025 GMT
Custom Metadata: no
Metadata Stream: yes
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           1
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       5363 bytes
Optimized:       no
PDF version:     1.7
```

We can see that this PDF file was created using _Typst_, searching for Typst we can quickly find the
documentation for the program [here](https://typst.app/docs/).

Reading the reference we can see that Typst has functionality for data loading, specifically it 
allows us to read arbitrary files within the project directory. So lets try and read the flag file.

```bash
echo '#read("flag.txt")' | nc domain port > give-flag-pls.pdf
```

Now if we open the PDF file using a PDF reader we should be presented with the flag!
