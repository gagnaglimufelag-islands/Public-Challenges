from flask import Flask
import hashlib
import os
import sys
import base64

app = Flask(__name__)

secret = os.urandom(16)

FLAG = os.environ.get("FLAG", "flag{temp_flag}")

@app.route('/token/<name>')
def get_token(name):
    name = base64.urlsafe_b64decode(name)
    
    if name.find(b'admin') != -1: return "Nope, admin is only for me"
    return base64.urlsafe_b64encode(hashlib.sha224(secret + name).digest())

@app.route('/login/<name>/<token>')
def login(name, token):
    token = base64.urlsafe_b64decode(token)
    name = base64.urlsafe_b64decode(name)

    hsh = hashlib.sha224(secret + name).digest()
    if hsh == token:
        if name.find(b'admin') != -1:
            return f"Hi Admin, here is the flag {FLAG}"
    request = hashlib.sha256(hsh).hexdigest()
    return f"Invalid request {request}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
