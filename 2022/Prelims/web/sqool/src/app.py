#!/usr/bin/env python3
from flask import Flask, Response, escape, request, render_template, flash, redirect, url_for, make_response, abort
import sqlite3
import secrets
import os
import base64
import hashlib
from pathlib import Path
from hashlib import sha512
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = secrets.token_bytes(10)

PUBLIC_HOST = os.environ.get('PUBLIC_HOST', 'localhost:5000')
SESSION_COOKIE_NAME = 'auth_session'
FLAG = os.environ.get('FLAG', 'falg{ThisIsNotYourFlag}')
MAX_ATTEMPTS = 5
HERE = Path(__file__).parent
DB = HERE / 'db.sqlite'

SESSIONS = {}

def digest(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def authenticate(username, pw):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    query = f"SELECT username FROM users WHERE username='{username}' and password='{digest(pw)}'"
    print(query)
    res = c.execute(query).fetchone()
    if res:
        return res[0]
    return res

def get_user_details(user):
    username = user['user']
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    query = f"SELECT username, email FROM users WHERE username='{username}'"
    print(query)
    res = c.execute(query).fetchone()
    return res

def get_auth():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    if user := SESSIONS.get(cookie):
        user.update(get_user_details(user))
        return user
    return None

@app.route('/login', methods=['GET','POST'])
def login():
    auth = get_auth()
    if auth:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        user = authenticate(username, request.form['password'])
        if not user:
            flash('Incorrect username or password', 'error')
            return redirect(url_for('login'))

        resp = make_response(redirect(url_for('mfa')))
        mfa_code = ''.join(secrets.choice('0123456789') for _ in range(6))
        session = secrets.token_urlsafe(12)
        session_encoded = base64.b64encode(session.encode()).decode()
        SESSIONS[session_encoded] = {'type': '2fa', '2fa_code': mfa_code, 'attempts': 0, 'user': user}
        resp.set_cookie(SESSION_COOKIE_NAME, session_encoded)
        print('MFA', mfa_code)
        resp.set_cookie('mfa', hashlib.sha256(mfa_code.encode()).hexdigest())
        return resp

    return render_template('login.html', auth=auth)


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')

    if cookie in SESSIONS:
        del SESSIONS[cookie]

    resp.set_cookie(SESSION_COOKIE_NAME, '', expires=0)
    return resp


@app.route('/2fa', methods=['GET', 'POST'])
def mfa():
    auth = get_auth()
    if not auth:
        return redirect(url_for('login'))

    if auth['type'] == 'full':
        return redirect(url_for('index'))

    if request.method == 'POST':
        code = request.form['code']
        if code != auth.get('2fa_code'):
            auth['attempts'] += 1
            if auth['attempts'] == MAX_ATTEMPTS:
                flash('Too many 2FA attempts. You have been logged out.', 'error')
                return logout()
            flash('Incorrect 2FA code.', 'error')
            return redirect(url_for('mfa'))

        auth['type'] = 'full'
        resp = redirect(url_for('index'))
        resp.set_cookie('mfa', '', expires=0)
        return resp

    return render_template('2fa.html')


@app.route('/')
def index():
    auth = get_auth()
    if auth and auth['type'] == '2fa':
        return redirect(url_for('mfa'))

    return render_template('index.html',
            auth=auth,
            flag=FLAG)


@app.route('/security.txt')
@app.route('/.well-known/security.txt')
def sec():
    resp = make_response('''Contact: mailto:security@hischool.is
Acknowledgments: https://hischool.is/hall-of-fame''')
    resp.mimetype = "text/plain"
    return resp


def setup_db():
    if DB.exists():
        DB.unlink()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('CREATE TABLE users (username text, email text, password text)')
    c.execute("INSERT INTO users (username, email, password) VALUES ('someone', 'someone@something.is', ?)", (digest(secrets.token_urlsafe(64)), ))
    c.execute("INSERT INTO users (username, email, password) VALUES ('nobody', 'no@body.com', ?)", (digest(secrets.token_urlsafe(64)), ))
    c.execute("INSERT INTO users (username, email, password) VALUES ('badmin', 'badmin@ton.us', ?)", (digest(secrets.token_urlsafe(64)), ))
    c.execute("INSERT INTO users (username, email, password) VALUES ('admin', 'admin@hischool.is', ?)", (digest(secrets.token_urlsafe(64)), ))
    c.execute("INSERT INTO users (username, email, password) VALUES ('wat', 'wat@wat.wat', ?)", (digest(secrets.token_urlsafe(64)), ))
    c.execute("INSERT INTO users (username, email, password) VALUES ('notmin', 'notmin@yahoo.com', ?)", (digest(secrets.token_urlsafe(64)), ))
    c.execute("INSERT INTO users (username, email, password) VALUES ('aadmin', 'aaadmin@hischool.com', ?)", (digest(secrets.token_urlsafe(64)), ))
    c.execute("INSERT INTO users (username, email, password) VALUES ('flagmin', 'gg{nicetry...', ?)", (digest(secrets.token_urlsafe(64)), ))
    conn.commit()
    conn.close()


setup_db()
