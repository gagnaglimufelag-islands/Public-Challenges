from Crypto.Util.number import long_to_bytes as ltb, bytes_to_long as btl
from multiprocessing import Pool, cpu_count
from urllib.parse import unquote
from ed25519 import SigningKey
from base64 import b64decode as b64d
from pathlib import Path
from tqdm import trange

import subprocess
import requests
import argparse
import hashlib
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

# with open('test2.id_ed25519') as f:

def brute(low, high, pk, origSk, report):
	rangeObj = trange(low, high) if report else range(low, high)
	for hidden in rangeObj:
		sk = origSk
		sk |= hidden << 236
		sk = ltb(sk).rjust(32, b'\x00')
		maybePk = SigningKey(sk)
		if maybePk.vk_s == pk:
			# print('===== Seed Found =====')
			# print(sk.hex())
			# break
			return sk

def test():
	with open(HERE / 'censored.id_ed25519') as f:
		data = ''.join(f.read().split('\n')[1:-1])
		data = b64d(data)

	pkPosition = 0x7d
	pkLen = 0x20
	pk = data[pkPosition:pkPosition + pkLen]
	print('public key: {}'.format(pk.hex()))

	skPosition = 0xa1
	skLen = 0x20
	origSk = data[skPosition:skPosition + skLen]
	origSk = btl(origSk)
	print('partial secret key: {}'.format(hex(origSk)[2:]))

	origSk &= 0x00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

	bruteRange = 0x100000
	cores = max(cpu_count() - 1, 1)
	params = []
	for core in range(cores):
		low = int(core * (bruteRange // cores))
		high = int((core + 1) * (bruteRange // cores))
		params.append((low, high, pk, origSk, core == 0))
	
	with Pool(cores) as p:
		cand = p.starmap(brute, params)
	
	flag = [elem for elem in cand if elem][0].hex()
	flag = 'gg{' + flag + '}'
	assert FLAG == flag, flag

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	parser = argparse.ArgumentParser()
	
	### STANDALONE ###
	test()
	### STANDALONE ###

