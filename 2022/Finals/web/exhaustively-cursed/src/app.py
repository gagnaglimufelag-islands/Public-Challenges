#!/usr/bin/env python3
from flask import Flask, request, render_template

import os
import re
import ipaddress
import requests


app = Flask(__name__)

FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")


# I just learned RegEx and how it can help me filter IPs!!!
IPV4 = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
RULES = [
    re.compile(r"10\.\d{1,3}\.\d{1,3}\.\d{1,3}"),
    re.compile(r"127\.\d{1,3}\.\d{1,3}\.\d{1,3}"),
    re.compile(r"192\.168\.\d{1,3}\.\d{1,3}"),
    re.compile(r"169\.254\.\d{1,3}\.\d{1,3}"),
]
# TODO IMPLEMENT LATER TODO
# 172 private network filtering is difficult to do in RegEx
# Simple hotfix while I develop a RegEx rule!!!
PRIVATE_172 = ipaddress.ip_network("172.16.0.0/12")


def validate_ip(ip):
    # Only allow IPs, security team told me that DNS is dangerous
    if not IPV4.fullmatch(ip):
        raise ValueError("Invalid IP")

    # RegEx to help me filter bad IPs >:(
    if any([rule.fullmatch(ip) for rule in RULES]):
        raise ValueError("Invalid IP")

    ip = ipaddress.ip_address(bytes(map(int, ip.split("."))))
    if ip in PRIVATE_172:
        raise ValueError("Invalid IP")

    return str(ip)


def is_local():
    return request.remote_addr == "127.0.0.1"


@app.route("/flag")
def flag():
    if not is_local():
        return render_template("403.html"), 403

    return render_template("flag.html", flag=FLAG)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ip = request.form["ip"]
        path = request.form["path"]

        if not ip:
            return render_template("index.html", error_message="No IP given")

        if not path:
            path = ""

        try:
            valid_ip = validate_ip(ip)
            print(valid_ip)
            result = requests.get(
                f"http://{valid_ip}{path}",
                timeout=1,
                allow_redirects=False,
                verify=False,
            ).content
            return render_template(
                "index.html",
                result=result.decode(),
                ip=valid_ip,
                path=path,
            )
        except ValueError as msg:
            return render_template("index.html", error_message=msg)
        except requests.exceptions.ConnectionError as e:
            print(e)
            return render_template("index.html", error_message="Website is dead")
        except:
            return render_template("index.html", error_message="Unexpected error")

    return render_template("index.html")
