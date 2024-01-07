#!/usr/bin/env python3
from flask import (
    Flask,
    request,
    redirect,
    url_for,
    flash,
    redirect,
    make_response,
    render_template,
)

import os
import base64
import secrets

import db

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

PUBLIC_HOST = os.environ.get("PUBLIC_HOST", "localhost:5000")
SESSION_COOKIE_NAME = "auth_session"
FLAG = os.environ.get("FLAG", "falg{ThisIsNotYourFlag}")
NAME = 0
CODE = 1
TYPE = 2

SESSIONS = {}

db.setup_db()


def get_auth():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, "")
    if user := SESSIONS.get(cookie):
        return user
    return []


@app.route("/login", methods=["GET", "POST"])
def login():
    auth = get_auth()
    if auth:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form["username"]
        user = db.authenticate(username, request.form["password"])
        if not user:
            flash("Incorrect username or password", "error")
            return redirect(url_for("login"))

        session = secrets.token_urlsafe(12)
        session_encoded = base64.b64encode(session.encode()).decode()
        if db.has_mfa(user):
            resp = make_response(redirect(url_for("mfa")))
            mfa_code = "".join(secrets.choice("0123456789") for _ in range(6))
            SESSIONS[session_encoded] = [user, mfa_code, "mfa"]

            resp.set_cookie(SESSION_COOKIE_NAME, session_encoded)
            return resp

        SESSIONS[session_encoded] = [user, "", "full"]
        resp = make_response(redirect(url_for("index")))
        resp.set_cookie(SESSION_COOKIE_NAME, session_encoded)
        return resp

    return render_template("login.html", auth=auth)


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("index")))
    cookie = request.cookies.get(SESSION_COOKIE_NAME, "")

    if cookie in SESSIONS:
        del SESSIONS[cookie]

    resp.set_cookie(SESSION_COOKIE_NAME, "", expires=0)
    return resp


@app.route("/mfa", methods=["GET", "POST"])
def mfa():
    if request.method == "POST":
        cookie = request.cookies.get(SESSION_COOKIE_NAME, "")
        user = SESSIONS.get(cookie)
        if not user:
            user = db.get_user_details(request.form["username"])

        code = request.form["code"]
        if code != user[CODE]:
            flash("Incorrect 2FA code.", "error")
            return logout()

        user[TYPE] = "full"
        session = secrets.token_urlsafe(12)
        session_encoded = base64.b64encode(session.encode()).decode()
        SESSIONS[session_encoded] = user

        resp = redirect(url_for("index"))
        resp.set_cookie("mfa", "", expires=0)
        resp.set_cookie(SESSION_COOKIE_NAME, session_encoded)
        return resp

    return render_template("mfa.html", auth=get_auth())


@app.route("/")
def index():
    auth = get_auth()
    if auth and auth[TYPE] == "mfa":
        return redirect(url_for("mfa"))
    return render_template("index.html", auth=auth, flag=FLAG)
