import os
from flask import Flask, redirect, render_template

FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/1")


@app.route("/<int:number>")
def dictating_director(number):
    if number < 6767:
        next_number = number + 1
        return redirect(f"/{next_number}")
    else:
        return render_template("win.html", flag=FLAG)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
