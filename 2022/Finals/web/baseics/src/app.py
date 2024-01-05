#!/usr/bin/env python3
from flask import Flask, request, render_template, redirect, url_for, make_response, flash
import secrets
import os
import logging
import base64
import subprocess
import time
from pathlib import Path

from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = secrets.token_bytes(10)
HERE = Path(__file__).parent
PUP = (HERE / 'pup' / 'pup.js').resolve()

logger = logging.getLogger('werkzeug')

FLAG = os.environ.get('FLAG', 'falg{NOTyourFLAG}')
SESSION_COOKIE_NAME = 'auth_session'

SESSIONS = {}

PIN_ORDER = list(range(7))
sr = secrets.SystemRandom()
sr.shuffle(PIN_ORDER)

RESULTS = {}

ENCODERS = {
    'b16': base64.b16encode,
    'b32': base64.b32encode,
    'b64': base64.b64encode,
    'a85': base64.a85encode,
}

BASES = [
    ('b16', 'Base16'),
    ('b32', 'Base32'),
    ('b64', 'Base64'),
    ('a85', 'Ascii85'),
]

def get_session():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    if cookie in SESSIONS:
        return SESSIONS[cookie]
    return None

def resp(text, status):
    response = make_response(text, status)
    response.mimetype = "text/plain"
    return response

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/results/<string:rid>', methods=['GET'])
def results(rid):
    res = RESULTS.get(rid)
    if not res:
        return redirect(url_for('index'))
    return render_template('index.html', bases=BASES, rid=rid, **res)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        res = {}
        base = request.form['base']
        if base not in ENCODERS:
            return redirect(url_for('index'))

        if f := request.files.get('file'):
            data = f.read()
            res['filename'] = f.filename
            res['file'] = data
        else:
            text = request.form['text']
            res['text'] = text
            data = text.encode()

        rid = secrets.token_urlsafe()

        RESULTS[rid] = {**res, 'base': base, 'result': ENCODERS[base](data).decode()}
        return redirect(url_for('results', rid=rid))

    return render_template('index.html', flag=FLAG, bases=BASES)


@app.route('/report', methods=['POST'])
def report():
    rid = request.form['result_id']
    if rid not in RESULTS:
        flash('That result does not exist', 'error')
        return redirect(url_for('index'))

    subprocess.Popen(['node', str(PUP), rid, FLAG])
    time.sleep(2)
    flash('That result looks good to us')
    return redirect(url_for('results', rid=rid))
