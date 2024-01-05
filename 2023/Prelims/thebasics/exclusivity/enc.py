import random

text = open("flag", "rb").read()
key = random.randint(1, 255)
encrypted = bytes([b ^ key for b in text])

with open("enc.txt", "wb") as f:
    f.write(encrypted)
