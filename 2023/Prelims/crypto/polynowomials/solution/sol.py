from polynomial import Polynomial
from urllib.parse import unquote
from pwn import *
from pathlib import Path
from tqdm import trange
from time import time
import subprocess
import requests
import argparse
import logging
import secrets
import select
import json
import yaml
import re

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?_{}'

# For local binary testing
def solve(conn):
	flag = ''
	flagLen = 69
	# idx = 0
	for idx in trange(flagLen):
		chars = set(alphabet)
		while len(chars) != 1:
			if len(chars) == 0:
				raise Exception('fuck')
			conn.recvuntil('Quit.\n')
			conn.sendline('c')
			conn.sendline(str(idx))
			polyArr = conn.recvline()[12:].strip().split(b' + ')
			# print(polyArr)
			polyArr = [coeff[:coeff.find(b'x')] if b'x' in coeff else coeff for coeff in polyArr][::-1]
			poly = Polynomial(list(map(int, polyArr)))
			recoveredChars = {char for char in alphabet if poly(ord(char)) == 0}
			chars &= recoveredChars
			# print(chars)
		flag += list(chars)[0]

	assert FLAG in flag, flag


### IF BINARY ###
def test(domain, port):
	sh = remote(domain, port)
	solve(sh)


if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	parser = argparse.ArgumentParser()
	
	### LOCAL BINARY ###
	parser.add_argument("domain", default="127.0.0.1", nargs="?")
	parser.add_argument("port", default=1337, type=int, nargs="?")
	args = parser.parse_args()
	sh = process(['python3', 'chall.py'])
	solve(sh)
	### LOCAL BINARY ###
