import requests
import subprocess
from fractus import sha2_256
from base64 import urlsafe_b64decode as decode
from base64 import urlsafe_b64encode as encode

padding = encode(b'a'+sha2_256.padding(17)+b'admin').decode()

s224_a =  ((requests.get(f'http://127.0.0.1:5000/token/{encode(b"a").decode()}').text))
s256_token = requests.get(f'http://127.0.0.1:5000/login/{padding}/{s224_a}').text.split(' ')[-1]
s224_a = decode(s224_a)

cmd = ['cargo', 'run', '--release', s224_a.hex(), s256_token]
result = subprocess.run(cmd, capture_output=True, text=True)
output = bytes(eval(result.stdout.strip()))
token = encode(output).decode()
print(requests.get(f'http://127.0.0.1:5000/login/{padding}/{token}').text)

