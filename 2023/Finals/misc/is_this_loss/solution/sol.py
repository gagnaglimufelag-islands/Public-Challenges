import re
import yaml
import logging
from math import ceil
from pathlib import Path
from base64 import b64decode

import cv2
import numpy as np
from pwn import *

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]
WIDTH = 32
HEIGHT = 32
FRIEND_RE = "iVBOR.*"
IS_THIS_LOSS = "./isthisloss.png"


def find_pos(friend):
    loss = cv2.imread(IS_THIS_LOSS)
    nparr = np.frombuffer(friend, np.uint8)
    find = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(loss, find, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    locs = np.where(res >= threshold)
    for pt in zip(*locs[::-1]):
        return (ceil(pt[0] / WIDTH), ceil(pt[1] / HEIGHT))  # Only need the first one


def parse_friend_from_msg(msg):
    return b64decode(re.search(FRIEND_RE, msg).group(0))


def solve(sh):
    sh.recvuntil(b"\n\n")  # Ignore banner
    for _ in range(5):
        msg = sh.recvuntil(b"> ")
        friend = parse_friend_from_msg(msg.decode())
        (x, y) = find_pos(friend)
        sh.sendline(f"{x}, {y}".encode())
        result = sh.recvline()
        assert result == b"Correct!\n", result

    flag = sh.recvline().decode()
    assert FLAG in flag, flag


def test(domain, port):
    sh = remote(domain, port)
    solve(sh)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test("localhost", 32000)
    # sh = process("./server.py")
    # solve(sh)
