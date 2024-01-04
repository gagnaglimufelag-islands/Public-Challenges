import base64
import secrets
import urllib
import urllib.request

from flask import (
    Flask,
    make_response,
    redirect,
    url_for,
    request,
    render_template,
    flash,
)
from flask_caching import Cache

from db import DB
import utils

config = {"CACHE_TYPE": "fast_cache.FastCache", "CACHE_DEFAULT_TIMEOUT": 10}

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config.from_mapping(config)
cache = Cache(app)

DBS = {}

def get_session():
    return request.cookies.get('instance')

def get_instance():
    sess = get_session()
    if sess not in DBS:
        DBS[sess] = DB(sess)
    return DBS[sess]


def db():
    return get_instance()

@app.before_request
def before_request_func():
    if not get_session():
        session = secrets.token_urlsafe(16)
        resp = redirect(request.url)
        resp.set_cookie('instance', session)
        return resp

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stats", methods=["GET"])
def stats():
    valid_blob = cache.get("content")
    if valid_blob:
        return render_template("stats.html", data=valid_blob)

    host = utils.validate_host(db().get_host())
    # Don't allow any weird stuff
    if not host:
        flash("Invalid host", "error")
        return render_template("stats.html", data=valid_blob)

    # Only support HTTP scheme, will add support for HTTPS in version 2.0
    url = f"http://{db().get_host()}:80/api/stats"
    try:
        content = urllib.request.urlopen(url).read()
        valid_blob = utils.validate_blob(content.decode())
        cache.set("content", valid_blob)
        if not valid_blob:
            flash("JSON blob is of invalid form", "error")
            return render_template("stats.html", data=valid_blob)
    except Exception as _:
        flash("Error fetching content from URL", "error")
        return render_template("stats.html", data=valid_blob)

    return render_template("stats.html", data=valid_blob)


@app.route("/logout", methods=["POST"])
def logout():
    resp = make_response(redirect(url_for("index")))
    cookie = request.cookies.get(utils.SESSION_COOKIE_NAME, "")

    if cookie in utils.SESSIONS:
        del utils.SESSIONS[cookie]

    resp.set_cookie(utils.SESSION_COOKIE_NAME, "", expires=0)
    return resp


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = db().authenticate(username, password)
        if not user:
            flash("Incorrect username or password", "error")
            return redirect(url_for("admin"))

        resp = make_response(redirect(url_for("change_host")))
        session = secrets.token_urlsafe(12)
        session_encoded = base64.b64encode(session.encode()).decode()
        utils.SESSIONS[session_encoded] = {
            "user": user,
        }
        resp.set_cookie(utils.SESSION_COOKIE_NAME, session_encoded)
        return resp

    return render_template("admin.html")


@app.route("/admin/change_host", methods=["GET", "POST"])
def change_host():
    if not utils.is_admin(request) and not utils.is_localhost(request):
        return redirect(url_for("index"))

    if request.method == "POST":
        new_host = request.form["host"]
        validated_host = utils.validate_host(new_host)
        if validated_host:
            db().set_host(new_host)
            flash("Host changed successfully!", "success")
            return redirect(url_for("change_host"))
        else:
            flash("Invalid host", "error")
            return redirect(url_for("change_host"))

    curr_host = db().get_host()
    return render_template("change_host.html", host=curr_host)
