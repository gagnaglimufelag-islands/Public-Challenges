from flask import render_template, request, json, jsonify, request, redirect, url_for, flash, Response, send_file, make_response
import os, requests, magic, time
from models import File
from app import app, ALLOWED_EXTENSIONS, db
from werkzeug.utils import secure_filename
from urllib.parse import unquote
from secrets import token_urlsafe
from pathlib import Path
import shutil

CLOUD = 'cloud'

def log(text):
    l = open("logs.txt","a")
    l.write(str(time.time()) +": " + text+"\n")
    l.close()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_session():
    session = request.cookies.get('session')
    if File.query.filter_by(session=session).count():
        return session
    return None


def init_session(session):
    here = Path(__file__).parent
    pfile = here / 'persistent_files'
    fileshare = here / 'files' / session
    fileshare.mkdir(exist_ok=True)
    for f in pfile.glob('*'):
        shutil.copy(f, fileshare)
    new_file = File('cute_cat.jpeg', session)
    db.session.add(new_file)
    db.session.commit()


@app.route('/cloud/list')
def file_list():
    if not (session := get_session()):
        return redirect(url_for('main'))

    files = File.query.filter_by(session=session)
    array = []
    for i in files:
        array.append({"filename":i.name,"id":i.id})
    return jsonify(array)


@app.route('/cloud/files')
def files():
    file_id = request.args.get('file_id')
    if file_id:
        files = File.query.get(file_id)
        return jsonify(files)
    return None


@app.route('/86266ee937d97f812a8e57d22b62ee29')
def reset():
    try:
        os.system("rm -f db.db && cp db.bak db.db")
    except Exception:
        log("Reset triggered")
        pass

    os.system('cd files && find . -not -name "index.html" -not -name "flag.txt" -not -name "cute_cat.jpeg" -delete')
    return "Reset done"


@app.route('/cloud/fetch')
def fetch():
    file_id = request.args.get('file_id')
    download = request.args.get('download')
    view = request.args.get("view")
    if file_id:
        try:
            r = requests.get(f'http://{CLOUD}/cloud/files?file_id={file_id}')
            if view:
                session = get_session()
                if session is None:
                    raise Exception('Missing session cookie')
                name = f"files/{session}/" + json.loads(r.text)['name']
                return send_file(name)

            if download:
                download_url = json.loads(r.text)['download_url']
                name = json.loads(r.text)['name']
                if ("txt" in name) or ("json" in name) or ("html" in name):
                    ct = {'Content-type':'text/plain'}
                else:
                    ct = {'Content-type':'image/png'}

                try:
                    d = requests.get(download_url)
                    raw = json.loads(d.content)['download_url']
                    f = requests.get(raw)
                    if "flag.txt" in json.loads(d.content)['download_url']:
                        log(unquote(str(request)) + str(json.loads(d.content)['download_url']))
                    return Response(f, headers=ct)

                except Exception as e:
                    log(unquote(str(request)) + str(e))
                    return Response(d.content, headers=ct)

            else:
                r = requests.get(f'http://{CLOUD}/cloud/files?file_id={file_id}')
                return Response(str(r.text), headers={'Content-type':'application/json'})

        except Exception as e:
            log(unquote(str(request)) + str(e))
            return Response(str(e), headers={'Content-type':'text/plain'})

    else:
        return "Error"


@app.route('/')
def main():
    resp = make_response(render_template('home.html', files=file_list()))
    if not get_session():
        session = token_urlsafe(8)
        init_session(session)
        resp.set_cookie('session', session)
    return resp


@app.route('/cloud/upload', methods=['GET', 'POST'])
def upload_file():
    if not (session := get_session()):
        return redirect(url_for('main'))

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename) and secure_filename(file.filename) != "flag.txt":
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], session, filename))
            new_file = File(filename, session)
            db.session.add(new_file)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                raise
            db.session.close()
            return "ok"
    return "nok"

