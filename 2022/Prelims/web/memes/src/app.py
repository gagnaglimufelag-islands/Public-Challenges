#!/usr/bin/env python3
from flask import Flask, Response, escape, request, render_template, flash, redirect, url_for, make_response
import string
import secrets
import os
import re
from urllib.parse import urlparse, quote
from hashlib import sha512
from werkzeug.middleware.proxy_fix import ProxyFix
from datetime import datetime

XSS_FILTER = re.compile(r'</?[\w="\']+/?>')

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = secrets.token_bytes(16)

ADMIN_PASS = os.environ.get('ADMIN_PASSWORD', 'asdf')
SESSION_COOKIE_NAME = 'auth_session'
FLAG = os.environ.get('FLAG', 'falg{ThisIsNotYourFlag}')

USERS = {
    'admin': {
        'pw': sha512(ADMIN_PASS.encode()).hexdigest(),
        'user': 'admin',
    }
}
if app.env == 'development':
    USERS['asdf'] = {
        'pw': sha512(b'asdf').hexdigest(),
        'user': 'asdf',
    }

SESSIONS = {}
TICKETS = []

AUTO_REJECT_AFTER = 5

def get_auth():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    if cookie in SESSIONS:
        return SESSIONS[cookie]
    return {}


@app.route('/login', methods=['GET','POST'])
def login():
    auth = get_auth()
    if auth:
        return redirect(url_for('index', title='Memes'))

    if request.method == 'POST':
        username = request.form['username']
        if username not in USERS:
            flash('Login error: User does not exist', 'error')
            return redirect(url_for('login', error=1))

        digest = sha512(request.form['password'].encode()).hexdigest()
        if digest != USERS[username]['pw']:
            flash('Login error: Password was not correct', 'error')
            return redirect(url_for('login', error=2))

        resp = make_response(redirect(url_for('index', title='Welcome to Memes!')))
        session = secrets.token_urlsafe(32)
        SESSIONS[session] = USERS[username]
        resp.set_cookie(SESSION_COOKIE_NAME, session)
        return resp

    return render_template('login.html', auth=auth)


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index', title='Sad to see you go')))
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    if cookie in SESSIONS:
        del SESSIONS[cookie]
    resp.set_cookie(SESSION_COOKIE_NAME, '', expires=0)
    return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
    auth = get_auth()
    if 'user' in auth:
        return redirect(url_for('index', title='Already meming'))

    if request.method == 'POST':
        username = request.form['username']
        if username in USERS:
            flash('Registration error: User already exists', 'error')
            return redirect(url_for('register'))
        if not set(username) <= set(string.ascii_letters + string.digits):
            flash('Registration error: Illegal username', 'error')
            return redirect(url_for('register'))

        USERS[username] = {
            'user': username,
            'pw': sha512(request.form['password'].encode()).hexdigest(),
        }
        flash('Registration successful. Go ahead and log in.')
        return redirect(url_for('login'))

    return render_template('register.html', auth=auth)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    auth = get_auth()
    title = request.args.get('title', 'Welcome to memes')
    # Filter out the bad things
    title = XSS_FILTER.sub('', title)
    if auth:
        if request.method == 'POST':
            name = request.form['name']
            url = request.form['url']
            error_message = None
            if not name or not url:
                flash('Both name and URL are required', 'error')
                return redirect(url_for('index'))
            if not name or not url:
                flash('Both name and URL are required', 'error')
                return redirect(url_for('index'))

            url_ok = False
            try:
                parsed = urlparse(url)
                if parsed.scheme in ('http', 'https'):
                    url_ok = True
                else:
                    flash('URLs must be valid and start with http(s)', 'error')
            except:
                flash('Horribly broken URL', 'error')

            if not url_ok:
                return redirect(url_for('index'))


            ticket = {
                'id': f'{auth["user"]}-{datetime.now().timestamp()}',
                'author': auth['user'],
                'name': name,
                'url': url,
                'status': 'pending',
                'timestamp': datetime.now(),
            }
            TICKETS.append(ticket)
            return redirect(url_for('index'))
        else:
            if auth['user'] != 'admin':
                tickets = [t for t in TICKETS if t['author'] == auth['user']]
            else:
                tickets = sorted([t for t in TICKETS if t['status'] == 'pending'], key=lambda x: x['timestamp'])[:1]
                if tickets:
                    tickets[0]['status'] = 'accepted'
            resp = Response(render_template('index.html',
                    error_message=error_message,
                    tickets=tickets,
                    auth=auth,
                    title=title,
                    flag=FLAG))
            return resp
    return render_template('index.html', auth=auth, title=title)
