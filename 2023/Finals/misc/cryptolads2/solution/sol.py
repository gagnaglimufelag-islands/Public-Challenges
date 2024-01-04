import requests
import argparse
import yaml
import logging
import re
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / 'meta.yml'))['flags']
OAST = re.compile(r'\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)')

logger = logging.getLogger('secretary')

def test(url):
    payload = r'''
import sys

def decrypt(ciphertext):
  sys.stdout.flush()
  print('\n'.join(open('stdout').read().splitlines()[:10]))
'''
    logger.debug('Payload: %s', payload)
    res = requests.post(f'{url}/submit', data={'code': payload})

    assert FLAG in (h := res.text), h

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', default='http://localhost:5000', nargs='?')
    args = parser.parse_args()

    test(args.url)
