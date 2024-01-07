import requests
import argparse
import yaml
import re
import subprocess
import logging
import secrets
import json
import select
from urllib.parse import unquote
from pwn import *
from time import time
from pathlib import Path

logger = logging.getLogger("secretary")

# For OOB interaction, if required
OAST = re.compile(r"\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


# For local binary testing
def solve(sh):
	print(sh.recvuntil(b'FLAG').decode())
	flag = sh.recvline().decode()
	assert FLAG in flag, flag

### IF BINARY ###
def test(domain, port):
	sh = process(['sage', 'babyLattice.sage', 'NOSPAMPLOX', f'DOMAIN={domain}', f'PORT={port}'], cwd=HERE)
	solve(sh)

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	parser = argparse.ArgumentParser()

	### LOCAL BINARY ###
	parser.add_argument("domain", default="127.0.0.1", nargs="?")
	parser.add_argument("port", default=1337, type=int, nargs="?") # @Hjalti plox put correct port here
	args = parser.parse_args()
	# print(f"sage babyLattice.sage NOSPAMPLOX DOMAIN='{args.domain}' PORT='{args.port}'")
	sh = process(['sage', 'babyLattice.sage', 'NOSPAMPLOX', f'DOMAIN={args.domain}', f'PORT={args.port}'], cwd=HERE)
	solve(sh)
	### LOCAL BINARY ###
