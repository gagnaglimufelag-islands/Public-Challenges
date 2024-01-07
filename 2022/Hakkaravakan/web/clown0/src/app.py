#!/usr/bin/env python3
from flask import (
    Flask,
    request,
    redirect,
    url_for,
    flash,
    make_response,
    render_template,
)

import os
import base64
import hashlib
import secrets
import sqlite3

from pathlib import Path

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

PUBLIC_HOST = os.environ.get("PUBLIC_HOST", "localhost:5000")
SESSION_COOKIE_NAME = "fishy_session"
FLAG = os.environ.get("FLAG", "falg{ThisIsNotYourFlag}")
HERE = Path(__file__).parent
DB = HERE / "db.sqlite"

SESSIONS = {}

BAD_CHARS = [" ", "-", "1", "="]
BAD_WORDS = [
    "or",
    "and",
    "having",
    "where",
    "like",
    "admin",
    "username",
    "email",
    "password",
]


def secure_hash(pw):
    return hashlib.sha256(pw.encode()).hexdigest()


# Make sure users can't do anything bad
def is_invalid(user_input):
    return any(c in user_input for c in BAD_CHARS) or any(
        w in user_input or w.upper() in user_input for w in BAD_WORDS
    )


def authenticate(username, pw):
    if is_invalid(username):
        return None

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    query = f"SELECT username FROM users WHERE password='{secure_hash(pw)}' AND username='{username}'"
    print(query)
    res = c.execute(query).fetchone()
    if res:
        return res[0]
    return res


def get_user_details(user):
    username = user["user"]
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    res = c.execute(
        "SELECT username, email FROM users WHERE username=?", (username,)
    ).fetchone()
    return res


def get_auth():
    cookie = request.cookies.get(SESSION_COOKIE_NAME, "")
    if user := SESSIONS.get(cookie):
        user.update(get_user_details(user))
        return user
    return None


@app.route("/login", methods=["GET", "POST"])
def login():
    auth = get_auth()
    if auth:
        return redirect(url_for("index"))

    if request.method == "POST":
        user = authenticate(request.form["username"], request.form["password"])
        if not user:
            flash("Incorrect username or password", "error")
            return redirect(url_for("login"))

        resp = make_response(redirect(url_for("index")))
        session = secrets.token_urlsafe(12)
        session_encoded = base64.b64encode(session.encode()).decode()
        SESSIONS[session_encoded] = {
            "user": user,
        }
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


@app.route("/")
def index():
    auth = get_auth()
    return render_template("index.html", auth=auth, flag=FLAG)


def setup_db():
    if DB.exists():
        DB.unlink()

    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("CREATE TABLE users (username text, email text, password text)")
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('fiskmundur', 'fiskmundur@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('evilnius', 'evilnius.morbius@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('admin', 'admin@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('phis', 'phis.william@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('pinky', 'pinky@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('kane', 'astounding.citizen@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('validuser', 'validuser@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    c.execute(
        "INSERT INTO users (username, email, password) VALUES ('ceoperson', 'ceo@fishy.is', ?)",
        (secure_hash(secrets.token_urlsafe(64)),),
    )
    conn.commit()
    conn.close()


setup_db()
