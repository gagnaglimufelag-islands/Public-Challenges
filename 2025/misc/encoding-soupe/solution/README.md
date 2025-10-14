# Cypher soupe

From the hint in the challenge description, it is likely that the author is referencing the Freemasonry. That can be used as a starter hint to the first cypher if you do not recognize it. Searching for `Freemasonry` and `cypher` should also provide the name of the cypher.

After decoding that we are left with a string that is b64 encoded and can be decoded easily. Inside that b64 encoded string lies braille that can be converted to text. This text can then be decyphered by running it through ROT13 which should be fairly visible due to how a ROT13 string looks. It retains accents from the original string such as two characters side by side are always encoded to the same characters and special characters are not always included in the alphabets used for encoding and decoding.


ENCODE> plaintext -> ROT13 -> Braille -> b64 -> pigpen

DECODE> pigpen -> b64 -> Braille -> ROT13 -> plaintext