#!/usr/bin/env python3
from flask import Flask, Response, escape, request, render_template, flash, redirect, url_for, make_response, abort
import secrets
import random
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = secrets.token_bytes(10)

FLAG = os.environ.get('FLAG', 'falg{ThisIsNotYourFlag}')
NFLAG = len(FLAG)

HITCH = '''
Bring it up
Check the rope
Spin around
On the neck
Whip it, whip it
Take it home
Bring it up, split it now
Shoulder, now, make a loop
Pull it, feed it, push it through
Up, stretch, down again
In the face and prepare
Lift, pull, bring it round
Thigh, tie, tighten tie
Kick the heel
Swivel time
Round, round, back to knot
C'mon!
Pull the loop
Down and through
Pull again
Lift the hand
Through the loop
Make a stitch
'''.strip().splitlines()

NHITCH = len(HITCH)
SESSIONS = {}


@app.route('/success')
def success():
    res = make_response(render_template('index.html', success=True))
    res.set_cookie('ctr_session', '')
    return res


@app.route('/fail')
def fail():
    res = make_response(render_template('index.html', success=False))
    res.set_cookie('ctr_session', '')
    return res

@app.route('/<letter>')
@app.route('/')
def redir(letter=''):
    session = request.cookies.get('ctr_session')

    if not session or session not in SESSIONS:
        redir = redirect('/')
        session = secrets.token_urlsafe()
        SESSIONS[session] = 0
        redir.set_cookie('ctr_session', session)
        return redir

    curr = SESSIONS[session]
    if curr == NFLAG:
        return redirect(url_for('success'))
    elif random.random() > 0.85:
        return redirect(url_for('fail'))

    SESSIONS[session] += 1
    resp = redirect(f'/{FLAG[curr]}')
    resp.mimetype = 'text/plain'
    resp.data = HITCH[curr % NHITCH]
    return resp

