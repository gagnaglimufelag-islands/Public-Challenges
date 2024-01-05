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
MAX_PLAYS = 100

CARDS = '🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎'

def rand_reds():
    return [secrets.choice([False, True]) for _ in range(3)]

def is_red(c):
    return CARDS.index(c) >= 26

class Game:
    def __init__(self):
        self.plays = 0
        self.wins = 0

        self.computer_seq = []
        self.player_seq = None
        self.deck = None
        self.flag = None
        self.done = False

    def reset(self):
        self.computer_seq = []
        self.player_seq = None
        self.deck = None
        self.flag = FLAG if (self.plays == MAX_PLAYS and self.wins == MAX_PLAYS) else None
        if self.plays >= MAX_PLAYS:
            self.done = True

    def start(self):
        if not self.computer_seq:
            self.computer_seq = rand_reds()

        return {
            'computer_seq': self.computer_seq_str,
            **self.status(),
        }

    def play(self, seq):
        self.player_seq = [s == 'R' for s in seq]
        drawn = []
        win = False

        while True:
            done = False
            c = list(CARDS)
            secrets.SystemRandom().shuffle(c)
            self.deck = c

            for i in range(3, len(c)):
                curr = list(map(is_red, c[i-3:i]))
                if curr == self.player_seq:
                    self.wins += 1
                    win = True
                    done = True
                    drawn = c[:i]
                    break

                elif curr == self.computer_seq:
                    done = True
                    drawn = c[:i]
                    break

            if done:
                self.plays += 1
                break

        self.reset()
        return {'win': win, 'draw': [{'card': c, 'red': is_red(c)} for c in drawn], **self.status()}

    def status(self):
        return {
            'plays': self.plays,
            'wins': self.wins,
            'flag': self.flag,
            'done': self.done,
        }

    @property
    def computer_seq_str(self):
        return ['BR'[i] for i in self.computer_seq]

def get_session():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    if cookie in SESSIONS:
        return SESSIONS[cookie]
    return None

def resp(text, status):
    response = make_response(text, status)
    response.mimetype = "text/plain"
    return response

@app.route('/api/start', methods=['POST'])
def guess():
    session = get_session()
    if not session:
        return {'error': 'Who are you?'}, 400

    res = session.start()

    return res

@app.route('/api/play', methods=['POST'])
def finish():
    session = get_session()
    if not session:
        return {'error': 'Who are you?'}, 400

    seq = (request.get_json() or {}).get('seq')
    if session.plays == MAX_PLAYS:
        return {'error': 'Game over'}, 400
    if seq and len(seq) == 3 and set(seq) <= set('RB'):
        return session.play(seq)
    else:
        return {'error': 'Invalid sequence. Must be a string of length three that contains only R and B.'}, 400


@app.route('/api/reset', methods=['POST'])
def reset():
    session = get_session()
    if not session:
        return {'error': 'new phone, who dis?'}, 400

    cookie = request.cookies.get(SESSION_COOKIE_NAME, '')
    SESSIONS[cookie] = Game()

    return {'success': True}

@app.route('/', methods=['GET','POST'])
def index():
    if not get_session():
        g = Game()
        g.start()
        resp = make_response(render_template('index.html', game=g))
        session = secrets.token_urlsafe(32)
        SESSIONS[session] = g
        resp.set_cookie(SESSION_COOKIE_NAME, session)
        return resp

    return render_template('index.html', game=get_session())

