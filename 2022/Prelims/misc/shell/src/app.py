#!/usr/bin/env python3
from flask import Flask, Response, escape, request, render_template, flash, redirect, url_for, make_response
import secrets
import os
import logging
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = secrets.token_bytes(10)

logger = logging.getLogger('werkzeug')

FLAG = os.environ.get('FLAG', 'falg{NotYourFlag}')
SESSION_COOKIE_NAME = 'game_session'

SESSIONS = {}

def random_pos():
    return secrets.choice([1,2,3])

class Game:
    def __init__(self):
        self.plays = 0
        self.correct = 0

        self.position = random_pos()
        self.guess = None
        self.empty = None
        self.swap = None
        self.last_result = None
        self.flag = None
        self.done = False

    def reset(self):
        self.position = random_pos()
        self.guess = None
        self.empty = None
        self.swap = None
        self.flag = FLAG if (self.plays <= 100 and self.correct >= 65) else None
        if self.plays >= 100:
            self.done = True

    def choose(self, guess):
        self.guess = int(guess)

        self.empty = secrets.choice(list({1,2,3} - {self.guess, self.position}))
        self.swap = ({1,2,3} - {self.guess, self.empty}).pop()

        return {
            'empty': self.empty,
            'swap': self.swap,
            **self.status(),
        }

    def complete(self, swap):
        if swap:
            self.guess = self.swap

        if self.guess == self.position:
            self.correct += 1
            self.last_result = 'Win'
        else:
            self.last_result = 'Loss'
        self.plays += 1

        self.reset()
        return self.status()

    def status(self):
        return {
            'plays': self.plays,
            'correct': self.correct,
            'guess': self.guess,
            'last_result': self.last_result,
            'flag': self.flag,
            'done': self.done,
        }


def get_session():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    if cookie in SESSIONS:
        return SESSIONS[cookie]
    return None

def resp(text, status):
    response = make_response(text, status)
    response.mimetype = "text/plain"
    return response

@app.route('/api/guess', methods=['POST'])
def guess():
    session = get_session()
    if not session:
        return {'error': 'Who are you?'}

    guess = request.get_json().get('guess')
    if not guess:
        return {'error': 'Guess missing'}

    if guess not in [1,2,3]:
        return {'error': 'Invalid guess'}

    if session.guess:
        return {'error': 'Game not completed'}

    res = session.choose(guess)

    return res

@app.route('/api/complete', methods=['POST'])
def finish():
    session = get_session()
    if not session:
        return {'error': 'Who are you?'}

    swap = request.get_json().get('swap')
    if swap not in [True, False]:
        return {'error': 'Invalid choice'}

    res = session.complete(swap)

    return res


@app.route('/api/reset', methods=['POST'])
def reset():
    session = get_session()
    if not session:
        return {'error': 'new phone, who dis?'}

    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    SESSIONS[cookie] = Game()

    return {'success': True}

@app.route('/', methods=['GET','POST'])
def index():
    if not get_session():
        g = Game()
        resp = make_response(render_template('index.html', game=g.status()))
        session = secrets.token_urlsafe(32)
        SESSIONS[session] = g
        resp.set_cookie(SESSION_COOKIE_NAME, session)
        return resp

    return render_template('index.html', game=get_session())

