from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from pathlib import Path
import shutil

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {  'png', 'jpg', 'jpeg', 'gif','cnf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

PORT = 80

if __name__ == "__main__":

    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    here = Path(__file__).parent
    pfile = here / 'persistent_files'
    fileshare = here / 'files'
    fileshare.mkdir(exist_ok=True)
    for f in pfile.glob('*'):
        shutil.copy(f, fileshare)

    from views import *

    app.run(host="0.0.0.0", port=PORT)
