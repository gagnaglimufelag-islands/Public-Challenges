#!/usr/bin/env python3
from flask import Flask, request, render_template, redirect, url_for, make_response
import base64
import os
import json
import hmac, hashlib
import string
import logging

app = Flask(__name__)

FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")
SESSION_COOKIE_NAME = "blog_auth"

## user info


def user_info():
    return ((u := get_auth()) and u) or "anon"


## monitoring

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logging.addLevelName(logging.INFO + 1, "FLAG")

from flask import g


def log_request(response, flag=False):
    user = user_info()
    ip = request.headers.get("x-forwarded-for") or request.remote_addr
    session = request.cookies.get(SESSION_COOKIE_NAME, "-")
    user_agent = request.headers.get("user-agent", "-")
    content_type = request.headers.get("content-type", "-")
    level = logging.INFO + flag
    logging.log(
        level,
        f'[{user}] {session} ({ip}) {request.method} "{request.url}" {response.status_code} {response.content_length} "{content_type}" {g.data} "{user_agent}" ',
    )


@app.before_request
def before_req():
    g.data = request.get_data()


@app.after_request
def after_req(response):
    if response.direct_passthrough:
        return response

    flag = FLAG.encode() in response.get_data()
    log_request(response, flag=flag)
    return response


## end monitoring

users = {
    "admin": "71LJhv2k1zc2Erir2cMJ",
}


def get_auth():
    auth = {}
    try:
        return json.loads(
            base64.b64decode(
                request.cookies.get(SESSION_COOKIE_NAME, "").encode()
            ).decode()
        )
    except:
        pass
    return auth


@app.route("/login", methods=["GET", "POST"])
def login():
    auth = get_auth()
    if "user" in auth:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form["username"]
        if username not in users:
            return redirect(url_for("login", error=1))

        if not hmac.compare_digest(
            hashlib.sha256(request.form["password"].encode()).hexdigest(),
            hashlib.sha256(users[username].encode()).hexdigest(),
        ):
            return redirect(url_for("login", error=2))

        resp = make_response(redirect(url_for("index")))
        auth_str = '{"user":"%s","is_admin":false}' % (username)
        resp.set_cookie(
            SESSION_COOKIE_NAME, base64.b64encode(auth_str.encode()).decode()
        )
        return resp

    error = request.args.get("error")
    error_message = None
    if error == "1":
        error_message = "Login error: User does not exist"
    if error == "2":
        error_message = "Login error: Password was not correct"
    if error == "3":
        error_message = "Registration successful. Go ahead and log in."
    return render_template("login.html", error_message=error_message, auth=auth)


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("index")))
    resp.set_cookie(SESSION_COOKIE_NAME, "", expires=0)
    return resp


@app.route("/register", methods=["GET", "POST"])
def register():
    auth = get_auth()
    if "user" in auth:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form["username"]
        if username in users:
            return redirect(url_for("register", error=1))
        if not set(username) <= set(string.ascii_letters + string.digits):
            return redirect(url_for("register", error=2))

        users[username] = request.form["password"]
        return redirect(url_for("login", error=3))

    error = request.args.get("error")
    error_message = None
    if error == "1":
        error_message = "Registration error: User already exists"
    if error == "2":
        error_message = "Registration error: Illegal username"
    return render_template("register.html", error_message=error_message, auth=auth)


@app.route("/")
def index():
    posts = [
        {
            "title": "My favorite programming languages",
            "author": "admin",
            "date": "2020/01/29 13:33:37",
            "published": False,
            "content": f"""\
                Hi everyone! In this blog post I wanted to tell you about my
                favorite programming languages.

                <ul>
                    <li>TODO: Write a list of my favorite programming languages</li>
                    <li>TODO: Remember to hide this secret before I publish the post: {FLAG}</li>
                </ul>
            """,
        },
        {
            "title": "About my blog",
            "author": "admin",
            "date": "2020/01/26 01:15:29",
            "published": True,
            "content": """\
                I wanted to tell you about the technology behind my blog, which
                I created all by myself. I used the programming language Python
                3, and the web framework Flask. It's a very simple web
                framework and really easy to quickly create a blog like this
                one. Alright, that's it for today. Talk to you later!
            """,
        },
        {
            "title": "Welcome to my new blog",
            "author": "admin",
            "date": "2020/01/23 14:07:58",
            "published": True,
            "content": """\
                Hello everyone, and welcome to my new blog!</br>
                My name is Wookie - nice to meet you. Here I will post all my
                ramblings!
            """,
        },
    ]
    return render_template("index.html", posts=posts, auth=get_auth())
