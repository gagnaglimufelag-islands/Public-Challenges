#!/usr/bin/env python3
from flask import Flask, render_template
import os
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash(
        "anextremelylongcommac0mpl3xanddifficulttoguesspassword"
    ),
    "john": generate_password_hash("SillyGoose42"),
    "jane": generate_password_hash("liverpool"),
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None


@app.route("/intranet")
@auth.login_required
def intranet():
    return render_template("intranet.html", auth=auth.current_user(), flag=FLAG)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
