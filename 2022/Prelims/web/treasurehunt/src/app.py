#!/usr/bin/env python3
from flask import Flask, escape, request, render_template, flash, redirect, url_for, make_response, Response

app = Flask(__name__)

@app.route('/')
def index():
    resp = Response(render_template('index.html'))
    resp.headers['X-Treasure'] = 'gg{b00tyIsInTHEIoftheBeeHolder'
    return resp
