import requests
import subprocess
import yaml
from pathlib import Path
from fractus import sha2_256
from base64 import urlsafe_b64decode as decode
from base64 import urlsafe_b64encode as encode

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def run_test(url):
    padding = encode(b'a'+sha2_256.padding(17)+b'admin').decode()

    s224_a =  ((requests.get(f'{url}/token/{encode(b"a").decode()}').text))
    s256_token = requests.get(f'{url}/login/{padding}/{s224_a}').text.split(' ')[-1]
    s224_a = decode(s224_a)

    cmd = ['cargo', 'run', '--release', s224_a.hex(), s256_token]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd='sol')
    output = bytes(eval(result.stdout.strip()))
    token = encode(output).decode()
    return requests.get(f'{url}/login/{padding}/{token}').text

def test(url):
    assert FLAG in run_test(url)

if __name__ == '__main__':
    print(run_test('http://127.0.0.1:5000'))
