import os
import secrets
import sqlite3
import sys
from functools import wraps
from hashlib import sha512

from flask import (
    Flask,
    Response,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

import setup_db

USER_ID = "user_id"
USERNAME = "username"
DATABASE = "mandown.db"
ADMIN_USER = "admin"
ALLOWED_KEYS = ("download_directory", "max_simultaneous_downloads", "auto_resume")

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
setup_db.setup_db()


def get_db():
    return sqlite3.connect(DATABASE)


def hash_password(password):
    return sha512(password.encode()).hexdigest()


def logged_in(username, password):
    conn = get_db()
    user = conn.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, hash_password(password)),
    ).fetchone()
    conn.close()

    if user:
        session[USER_ID] = user[0]
        session[USERNAME] = user[1]
        return True
    return False


def get_config():
    conn = get_db()
    configs = conn.execute("SELECT key, value FROM config").fetchall()
    conn.close()
    return {row[0]: row[1] for row in configs}


def get_downloads():
    conn = get_db()
    conn.row_factory = sqlite3.Row
    downloads = conn.execute("SELECT * FROM downloads").fetchall()
    conn.close()
    return [dict(download) for download in downloads]


def requires_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if USER_ID not in session or session[USERNAME] != ADMIN_USER:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


@app.errorhandler(404)
def page_not_found(e):
    return render_template("invalid.html", title="Page not found"), 404


@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html", title="Welcome")


@app.route("/login", methods=["GET", "POST"])
def login():
    if USER_ID in session:
        return redirect(url_for("/dashboard"))
    if request.method == "GET":
        return render_template("login.html", title="Login")

    username = request.form["username"]
    password = request.form["password"]
    if logged_in(username, password):
        return redirect(url_for("dashboard"))

    flash("Failed to login!")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/system/version")
def get_version():
    conn = get_db()
    _, version = conn.execute(
        "SELECT key, value FROM config WHERE key = 'version'"
    ).fetchone()
    conn.close()
    return version


@app.route("/dashboard")
@requires_admin
def dashboard():
    downloads = get_downloads()
    total_downloads = len(downloads)
    status_values = [download["status"] for download in downloads]
    download_summary = {
        "total_downloads": total_downloads,
        "completed": status_values.count("completed"),
        "in_progress": status_values.count("in_progress"),
        "failed": status_values.count("failed"),
    }
    return render_template(
        "dashboard.html", title="Dashboard", summary=download_summary
    )


@app.route("/downloads")
@requires_admin
def downloads():
    downloads = get_downloads()
    return render_template("downloads.html", title="Downloads", downloads=downloads)


@app.route("/render", methods=["GET"])
def render():
    try:
        template = request.args.get("template")
        path = os.path.join("test_templates", template)
        data = render_template(path)
    except:
        data = render_template("invalid.html", title="Oops")
    return Response(data, mimetype="text/html")


@app.route("/set-config", methods=["POST"])
@requires_admin
def set_config():
    data = request.form
    if not data:
        flash("Invalid input: no data provided", "error")
        return redirect(url_for("system"))

    conn = get_db()
    cursor = conn.cursor()

    for k, v in data.items():
        if v == "":
            continue

        if k not in ALLOWED_KEYS:
            flash("Invalid input: invalid key entered", "error")
            return redirect(url_for("system"))

        cursor.execute(
            """
            INSERT INTO config (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value = excluded.value
            """,
            (k, v),
        )
    conn.commit()
    conn.close()
    flash("Config updated successfully!", "success")
    return redirect(url_for("system"))


@app.route("/system")
@requires_admin
def system():
    system_info = {
        "python": sys.version,
        "os": f"{os.name} - {sys.platform}",
        "config": get_config(),
        "username": session[USERNAME],
    }
    return render_template(
        "system.html", **system_info, allowed_keys=ALLOWED_KEYS, title="System"
    )
