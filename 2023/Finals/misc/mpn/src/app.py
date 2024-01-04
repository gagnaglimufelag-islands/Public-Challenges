#!/usr/bin/env python3
from flask import Flask, Response, escape, request, render_template, flash, redirect, url_for, make_response, abort
import secrets
import subprocess
import tempfile
import os
from pathlib import Path
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
app.secret_key = secrets.token_bytes(10)

FLAG = os.environ.get('FLAG', 'falg{ThisIsNotYourFlag}')
HERE = Path(__file__).parent

SESSIONS = {}

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

@app.route('/', methods=['POST', 'GET'])
def index():

    results = ''
    package = ''
    stderr = ''
    if request.method == 'POST':
        if not (package := request.form.get('package')):
            flash('Package must be specified', 'error')
        else:
            with tempfile.TemporaryDirectory() as td:
                try:
                    process = subprocess.run(['npm', 'install', package], cwd=td, timeout=10, capture_output=True, universal_newlines=True)
                    process.check_returncode()
                    total = sum([os.path.getsize(p) for p in  (Path(td) / 'node_modules').glob('**/*') if p.is_file()])
                    results = sizeof_fmt(total)
                except subprocess.TimeoutExpired:
                    flash('Installation took to long', 'error')
                except subprocess.CalledProcessError:
                    stderr = process.stderr
                    flash('''Error installing package. Does it exist?''', 'error')


    return render_template('index.html', flag=FLAG, package=package, results=results, stderr=stderr)
