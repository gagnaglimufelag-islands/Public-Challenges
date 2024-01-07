from flask import Flask, request, make_response
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
from os import path
import requests
import shutil
import socket

app = Flask(__name__)

def CheckFolder(IP):
    return path.exists(IP)

def MakeFolder(IP):
    shutil.copytree("BaseDir", IP)

def ClearFolder(IP):
    shutil.rmtree(IP)

def ReadIndex(IP):
    with open(IP + "/index.html", 'r', encoding='utf8') as f:
        return f.read()

def ReadFile(IP, file):
    if path.realpath(IP + file).startswith(path.realpath(IP)):
        try:
            with open(IP + file, 'r', encoding='utf8') as f:
                return f.read()
        except IsADirectoryError:
            file = file if file.startswith('/') else ('/' + file)
            if file == "/":
                with open(IP + "/index.html", 'r', encoding='utf8') as f:
                    return f.read()+" "
    else:
        raise Exception("path traversal")

@app.route('/', methods=['GET', 'OPTIONS', 'PUT'])
def entry_point():
    Method = request.method
    IP = request.headers.get('X-Forwarded-For') or request.environ['REMOTE_ADDR']

    if not CheckFolder(IP):
        MakeFolder(IP)

    if Method == "GET":
        return ReadIndex(IP)
    elif Method == "OPTIONS":
        resp = make_response()
        resp.headers["Allow"] = "GET, OPTIONS, PUT"
        return resp
    elif Method == "PUT":
        with open(IP + "/index.html", 'w', encoding='utf8') as f:
            URL = request.args.get('url')
            host = urlparse(URL)
            isLocal = (host.netloc == request.host or host.netloc == "127.0.0.1" or host.netloc == "127.0.0.1:55655") # Replace with actual port
            if isLocal:
                f.write(ReadFile(IP, host.path))
                f.close()
                return "Done"
            if URL:
                URL = URL if URL.startswith('http') else ('http://' + URL)
                print(URL)
                f.write(requests.get(url = URL).text)
            else:
                return "url parameter is missing."
        f.close()
        return "Done"

@app.route('/flag')
def flag():
    return "no flag for u"

@app.route('/reset')
def reset():
    IP = request.headers.get('X-Forwarded-For') or request.environ['REMOTE_ADDR']
    ClearFolder(IP)
    MakeFolder(IP)
    return "Reset!"

#Used to determine if a url is local or not in the PUT
@app.route("/KKAK")
def a():
    return "TRUE"
