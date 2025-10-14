# Running through the bases

This challenge revolves around figuring out which encodings are used. The string that is formatted is always using a format of `encoded_string,base`. Then we can take that, parse the string into two parts and try to decode. That reveals another string of the same format as the first one. Repeat this untill a flag appears.

This may take some trial and error to figure out all bases used to encode the string.
