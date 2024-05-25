#!/usr/bin/env python3
from flask import Flask, request, render_template, flash, redirect, url_for, make_response
import os
import string
from pathlib import Path
import sqlite3
import random
import yaml
import logging
import time
from flask.logging import default_handler

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger('website')

app = Flask(__name__)
app.logger.removeHandler(default_handler)

HERE = Path(__file__).parent.resolve()
FLAG = yaml.safe_load(open(HERE / '../meta.yml'))['flags']

HERE = Path(__file__).parent
DB = HERE / 'db.sqlite'

def randstr(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def get_flags(start):
    logger.info('Query: %s' % start)
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    query = f"SELECT item FROM items WHERE hidden=0 and item='{start}'"

    t0 = time.time()
    logger.info('SQL: %s', query)
    res = list(c.execute(query))
    t1 = time.time()
    logger.info(f'Query performance of [redacted for privacy]: {t1-t0} sec')
    return res

@app.route('/', methods=['GET', 'POST'])
def index():
    results=[]
    error_message = None
    start = ''
    if request.method == 'POST':
        start = request.form.get('query')
        if start:
            try:
                results = [res[0] for res in get_flags(start)]
                if not results:
                    error_message = 'Nothing found'
                    return render_template('index.html', results=results, start=start or '', error_message=error_message), 404
            except Exception as e:
                error_message = e.args[0]
                return render_template('index.html', results=results, start=start or '', error_message=error_message), 500
    return render_template('index.html', results=results, start=start or '', error_message=error_message)

def setup_db():
    if DB.exists():
        DB.unlink()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('CREATE TABLE items (item text, hidden int)')
    flags = [( f'{randstr(4)}{{{randstr(10)}}}', 0) for _ in range(5)]
    c.executemany("INSERT INTO items (item, hidden) VALUES (?, ?)", flags)
    c.execute('CREATE TABLE users (username text, password text)')
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', FLAG))
    conn.commit()
    conn.close()

setup_db()
