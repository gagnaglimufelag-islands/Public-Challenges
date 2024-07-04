## Shasha

Looking at `app.py`, we can see that the goal is to get the string `admin` into the name variable.

However since the name is being verified by a sha224 token that is generated by the token endpoint, we need to somehow find a valid sha224 hash with the admin string in it with a valid secret prefix.

This can be done using a length extension attack (LEA) on sha224, however since sha224 is a truncated version of sha256 with different inital values, there is no way to recover the hash state without guessing the last 4 bytes of the original sha256 (with changed iv) hash.

Therefore we need to brute force every 4 byte combination, appended to the sha224 hash and perform a sha256 (with changed iv) LEA on that hash.

So the process is like this, first send some name to the token endpoint like `encode('a')` (where encode is base64 encoding function).

Then send `encode('a'+sha256_padding(17)+'admin')` as the name to the login endpoint to get a sha256 hash of the sha224 hash we want to find.

Then brute force the 4 bytes for the sha224 hash and perform LEA on it, appending `'admin'` to the hash and then checking it against the sha256 we got from the login endpoint and then when that hash is found, submit the `encode('a'+sha256_padding(17)+'admin')` and sha224 hash to the login endpoint to get the flag.

To perform the LEA on sha224 you can just find an implementation of sha256 LEA and change the IV to the sha224 values.

An implementation of this solution can be found in `sol/`
