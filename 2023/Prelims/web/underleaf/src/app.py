from flask import Flask, request, make_response, render_template
from io import BytesIO
import subprocess
import tempfile

application = Flask(__name__)

@application.route('/')
def index():
  return render_template('index.html')

@application.route('/genpdf', methods=['POST'])
def generate_pdf():
  text = request.form.get('text')
  if not text:
    return 'No text provided', 400
  else:
    dirpath = tempfile.mkdtemp()
    proc = subprocess.Popen(['pdflatex', '-shell-escape', '-jobname=output'], cwd=dirpath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = proc.communicate(input=text)
    if proc.returncode != 0:
      print(stdout)
      return 'Error generating PDF', 500

    with open(dirpath+'/output.pdf', 'rb') as f:
      pdf_data = f.read()
    response = make_response(pdf_data)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=generated.pdf'
    return response

if __name__ == '__main__':
  application.run(host='0.0.0.0', port=5000, threaded=True)