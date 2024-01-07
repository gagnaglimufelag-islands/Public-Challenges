from flask import Flask, request, Response, render_template

import os

app = Flask(__name__)

FLAG = os.environ.get('FLAG', 'gg{1_l0v3_f14gl3_p4rk3r_fl4g}')

COUNTS = {}

for i in FLAG:
    if not i in COUNTS:
        COUNTS[i] = 0
    COUNTS[i] += 1

def wordle_checker(word):
    results = []
    local_counts = {}
    for i in range(len(word)):
        if word[i] == FLAG[i]:
            if not word[i] in local_counts:
                local_counts[word[i]] = 0
            local_counts[word[i]] += 1
            results.append("y")
            continue
        if word[i] in FLAG:
            if not word[i] in local_counts:
                local_counts[word[i]] = 0
            local_counts[word[i]] += 1
            if local_counts[word[i]] > COUNTS[word[i]]:
                results.append("n")
            else:
                results.append("?")
            continue
        results.append("n")
    return results

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/check/<word>")
def check(word):
    response = Response("".join(wordle_checker(word)))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/getflag")
def getflag():
    return "prankd"
