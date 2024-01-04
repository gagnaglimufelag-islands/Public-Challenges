from Crypto.Util.number import long_to_bytes as ltb
from urllib.parse import unquote
from multiprocessing import Pool, cpu_count
from hashlib import sha256
from pwn import *
from pathlib import Path
# from tqdm import trange
from time import time
import subprocess
import requests
import argparse
import secrets
import logging
import yaml #soyml
import select
import json
import re

logger = logging.getLogger("secretary")

# For OOB interaction, if required
OAST = re.compile(r"\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def passwordBasedKeyDerivationFunction(password, iterations = 69):
	for _ in range(iterations):
		password = sha256(password + b'Watame Factory!').digest()
	
	return password


### IF STANDALONE (i.e. work on chall.txt) ###
def brute(data, bruteRange):
	keyLen = 32
	for x in bruteRange:
		password = bytearray(passwordBasedKeyDerivationFunction(ltb(x)))
		if data[0] ^ password[0] == 103 and data[1] ^ password[1] == 103 and data[2] ^ password[2] == 123:
			s = ''.join(map(chr, [data[idx] ^ password[idx % keyLen] for idx in range(len(data))]))
			# s = ''.join(map(chr, [data[idx] ^ password[idx % 1] for idx in range(len(data))]))
			return s
def test():
	with open(HERE / 'flag.txt.enc', 'rb') as f:
		data = bytearray(f.read())
	
	passLen = 2
	bruteRange = 2**(passLen * 8)
	cores = max(cpu_count() - 1, 1)
	params = []
	for core in range(cores):
		tmp = range(int(core * (bruteRange // cores)),  int((core + 1) * (bruteRange // cores)))
		params.append((data, tmp))
	with Pool(cores) as p:
		cand = p.starmap(brute, params)
	
	assert FLAG in cand, cand


if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	parser = argparse.ArgumentParser()
	
	### STANDALONE ###
	test()
	### STANDALONE ###
