from flask import Flask, request, render_template
from queue import Queue, Empty
import os
import subprocess

app = Flask(__name__)

solution_timeout = 5 # seconds
mem_cap = 100*1024 # KiB
box_count = 5

FLAG = os.environ.get('FLAG', 'falg{n0tyourflag}')

with open('./evaluate.py', 'r') as f:
    EVALUATE_PY = f.read()

boxes = Queue()
for box in range(box_count):
    boxes.put(box)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    if 'code' not in request.form:
        return 'Missing code parameter'

    code = request.form['code']

    print('PAYLOAD')
    print(code)
    print('END OF PAYLOAD')

    try:
        box = boxes.get(timeout=30)
    except Empty:
        app.logger.error('TIMEOUT')
        return 'There was an error evaluating your submission. Please let us know.'
    try:
        subprocess.call(['isolate', '-b', str(box), '--cleanup'])
        path = subprocess.check_output(['isolate', '-b', str(box), '--init']).decode('ascii').strip()

        with open(path + '/box/evaluate.py', 'w') as f:
            f.write(EVALUATE_PY)

        with open(path + '/box/solution.py', 'w') as f:
            f.write(code)

        meta_path = '/tmp/box-%d-meta' % box

        subprocess.call(['isolate',
            '-b', str(box),
            '-t', str(solution_timeout),
            '-w', str(solution_timeout),
            '--stdout', '/box/stdout',
            '--stderr', '/box/stderr',
            '--mem', str(mem_cap),
            '--meta', meta_path,
            '--run', '--', '/usr/local/bin/python', 'evaluate.py'])

        with open(path + '/box/stdout', 'rb') as f:
            stdout = f.read()
        with open(path + '/box/stderr', 'rb') as f:
            stderr = f.read()

        meta = {}
        with open(meta_path, 'r') as f:
            for line in f:
                line = line.rstrip('\n')
                if ':' in line:
                    k,v = line.split(':', 1)
                    meta[k] = v

        try:
            subprocess.call(['isolate', '-b', str(box), '--cleanup'])
        except:
            import traceback
            app.logger.error(traceback.format_exc())

        if meta.get('status') == 'TO':
            return (stderr + b'\n\n' + b'Solution took too long to finish').lstrip(b'\n')
        if meta.get('status') == 'SG':
            return (stderr + b'\n\n' + b'Solution was killed (maybe it used too much memory?)').lstrip(b'\n')
        if meta.get('status') == 'RE':
            return (stderr + b'\n\n' + b'Solution crashed').lstrip(b'\n')

        if stderr:
            return (stderr + b'\n\n' + b'Something seems to have gone wrong').lstrip(b'\n')

        parts = stdout.split(b'------------------------- SEP -------------------------')
        if len(parts) != 2:
            return b'Hacking detected! Were you trying something silly!?'

        expected_raw, obtained_raw = parts
        expected = expected_raw.strip().splitlines()
        obtained = obtained_raw.strip().splitlines()
        N = len(expected)

        out = []

        for i, (ex, ob) in enumerate(zip(expected, obtained)):
            out.append('======== Test case %d/%d ========' % (i+1, N))
            if ex == ob:
                out.append('OK')
            else:
                out.append(f"Expected '{ex.decode(errors='backslashreplace')}' but got '{ob.decode(errors='backslashreplace')}'")
                break
        else:
            out.append(FLAG)

        return '\n'.join(out)
    except:
        import traceback
        app.logger.error(traceback.format_exc())
        return 'There was an error evaluating your submission. Please let us know.'
    finally:
        boxes.put(box)

