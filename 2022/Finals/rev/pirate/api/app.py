from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def nope():
    return "ERR"


@app.route("/53cr37_k3y")
def gib_flag():
    secret = request.headers.get("Secret-Key")
    if secret == "0d4r74ucd_4rrrlp46_3m__13A1nr__5":
        return "Flag: gg{4h0y_4rrgh_y4rr_g4r_4y3_4y3}"
    return "ERR"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
