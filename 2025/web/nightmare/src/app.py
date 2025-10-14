import re

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.errorhandler(404)
@app.errorhandler(500)
@app.route("/<path:unknown_path>")
def error(unknown_path=None):
    return render_template("error.html"), 404


@app.route("/debug")
def debug():
    filename = request.args.get("filename", "")
    if (
        filename == ""
        or not filename.startswith("/pro")
        or re.match(r"/pro./\d+", filename) is None
    ):
        return render_template("error.html")

    try:
        with open(filename, "r") as f:
            return str(eval(f.read()))
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
