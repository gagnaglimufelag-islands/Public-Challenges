from flask import (
    Flask,
    request,
)

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app.logger.info(request.form)
        return 'Data received, thank you!'
    return 'This is just a placeholder service, no hacking necessary'


