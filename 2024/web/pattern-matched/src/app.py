import re
import secrets
import sqlite3
from pathlib import Path

from flask import (
    Flask,
    redirect,
    url_for,
    request,
    render_template,
    flash,
)


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

HERE = Path(__file__).parent
CONN = sqlite3.connect(HERE / "db.sqlite", check_same_thread=False)
TOKEN_VALIDATION = re.compile(r"^[\[A-Za-z0-9\]+(_)?\[A-Za-z0-9\]+]{32,128}$")
CHECK_TOKEN_QUERY = "SELECT valid FROM tokens WHERE valid = TRUE %token"
GET_PATTERNS_QUERY = "SELECT name, pattern FROM patterns"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/patterns", methods=["GET"])
def patterns():
    free = request.args.get("free", default=False, type=lambda x: x.lower() == 'true')
    token = request.args.get("token")

    if free:
        return render_template("free.html")

    if not token:
        flash("Missing token!", "error")
        return redirect(url_for("index"))

    if not TOKEN_VALIDATION.fullmatch(token):
        flash("Invalid token!", "error")
        return redirect(url_for("index"))

    cur = CONN.cursor()
    res = cur.execute(
        CHECK_TOKEN_QUERY.replace("%token", f"AND token LIKE '{token}'")
    ).fetchone()

    if not res:
        flash("Invalid token!", "error")
        return redirect(url_for("index"))

    patterns = cur.execute(GET_PATTERNS_QUERY).fetchall()
    return render_template("patterns.html", patterns=patterns)
