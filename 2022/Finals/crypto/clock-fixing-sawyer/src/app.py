#!/usr/bin/env python3
from flask import Flask, request, render_template, redirect, url_for, make_response
import secrets
import os
import logging
import time
import math
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = secrets.token_bytes(10)

logger = logging.getLogger('werkzeug')

FLAG = os.environ.get('FLAG', '')
SESSION_COOKIE_NAME = 'auth_session'

SESSIONS = {}

PIN_ORDER = list(range(7))
sr = secrets.SystemRandom()
sr.shuffle(PIN_ORDER)

def password_hash(pw):
    # Use python's inbuilt hash function for efficiency and other nice
    # properties
    return (hash(pw)).to_bytes(8, 'big', signed=True)[1:]

ADMIN_PASS = password_hash(secrets.token_urlsafe())

def secure_hash_comparison(h1, h2):
    '''
    Securely compares two byte hashes, h1 and h2.

    The comparison is done in a random order. If mismatch is found, random
    sleep is introduced. These two factors should mitigate against side-channel
    attacks and brute force attacks.
    '''
    for index in PIN_ORDER:
        if h1[index] != h2[index]:
            time.sleep(math.ceil(h2[index] / 150) / 10)
            return False
    return True


def get_session():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    if cookie in SESSIONS:
        return SESSIONS[cookie]
    return None

def resp(text, status):
    response = make_response(text, status)
    response.mimetype = "text/plain"
    return response

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')


    if not (username and password):
        return {'error': 'Username or password missing', 'success': False}, 400

    if username != 'admin':
        return {'error': 'Unknown user', 'success': False}, 400

    if secure_hash_comparison(ADMIN_PASS, password_hash(password)):
        resp = make_response({'success': True})
        sess = secrets.token_urlsafe()
        resp.set_cookie(SESSION_COOKIE_NAME, sess)
        SESSIONS[sess] = {'username': 'admin'}
        return resp

    return {'error': 'Incorrect password', 'success': False}, 400

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/', methods=['GET'])
def index():
    if not get_session():
        return redirect(url_for('login'))
    return render_template('index.html', user=get_session(), flag=FLAG)
