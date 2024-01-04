#!/usr/bin/env python3
import os
import base64
import secrets
from hashlib import md5

from flask import Flask, render_template, request, Response

app = Flask(__name__)
app.secret_key = secrets.token_bytes(16)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 2048  # Max image size of 2MB
FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = [".jpg", ".png", ".gif"]
ALLOWED_CONTENT_TYPES = ["image/jpeg", "image/png", "image/gif"]
IMAGEMAGICK_VERSION = "ImageMagick 7.1.0-38"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


def convert(filepath, filename):
    resized_path = f"{UPLOAD_FOLDER}/resized_{filename}"
    os.system(f"./convert {filepath} -resize 128x128 {resized_path}")
    os.system(
        f"./convert {resized_path} -set Software '{IMAGEMAGICK_VERSION}' {resized_path}"
    )

    with open(f"{resized_path}", "rb") as f:
        data = f.read()

    os.remove(filepath)
    os.remove(resized_path)

    return base64.b64encode(data).decode()


@app.route("/upload", methods=["POST"])
def upload():
    if "picture" not in request.files:
        return Response(
            '{"success": false, "msg": "Missing file"}',
            mimetype="application/json",
            status=400,
        )
    picture = request.files["picture"]

    filename = picture.filename
    if filename is None:
        return Response(
            '{"success": false, "msg": "Missing filename"}',
            mimetype="application/json",
            status=400,
        )

    extension = os.path.splitext(filename)[1]
    if extension not in ALLOWED_EXTENSIONS:
        return Response(
            '{"success": false, "msg": "Invalid filetype"}',
            mimetype="application/json",
            status=400,
        )

    content_type = picture.headers["Content-Type"]
    if content_type not in ALLOWED_CONTENT_TYPES:
        return Response(
            '{"success": false, "msg": "Invalid filetype"}',
            mimetype="application/json",
            status=400,
        )

    tmp_name = f"{md5(filename.encode()).hexdigest()}{extension}"
    filepath = os.path.join(UPLOAD_FOLDER, f"{tmp_name}")

    picture.save(filepath)
    emoji = convert(filepath, tmp_name)

    return Response(
        f'{{"success": true, "emoji": "data:{content_type};base64,{emoji}"}}',
        mimetype="application/json",
    )
