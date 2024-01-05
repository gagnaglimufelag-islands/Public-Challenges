#!/usr/bin/env python3
from flask import Flask, render_template, request
import os

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")

WAT = "WAT"


def check_watness(request):
    if WAT not in request.args:
        return "WAT missing from query"
    elif request.args[WAT] != WAT:
        return "WAT missing from WAT query argument"
    elif WAT not in request.form:
        return "WAT missing from body"
    elif request.form[WAT] != WAT:
        return "WAT missing from WAT body argument"
    elif WAT not in request.cookies:
        return "WAT missing from cookies"
    elif request.cookies[WAT] != WAT:
        return "WAT missing from WAT cookie"
    elif WAT not in request.headers["User-Agent"]:
        return "You aren't using the WAT browser, please change the user agent"
    elif WAT not in request.headers:
        return "WAT header missing"
    elif request.headers[WAT] != WAT:
        return "WAT missing from WAT header"
    return FLAG


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/WAT", methods=["GET", "WAT"])
def wat():
    msg = None
    if request.method != WAT:
        msg = "This needs to be a WAT request"
        return render_template("wat.html", msg=msg)
    msg = check_watness(request)
    return render_template("wat.html", msg=msg)
