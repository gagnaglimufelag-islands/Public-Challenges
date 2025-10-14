# pyright: basic
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FLAG_SRC = Path(__file__).parent / "flag.txt"


def main():
    data = input()

    with tempfile.TemporaryDirectory() as tmpdir:
        typst_input = os.path.join(tmpdir, "input.typ")
        pdf_output = os.path.join(tmpdir, "output.pdf")
        flag_dst = os.path.join(tmpdir, "flag.txt")

        shutil.copyfile(FLAG_SRC, flag_dst)

        with open(typst_input, "wb") as f:
            f.write(data.encode())

        try:
            subprocess.run(
                ["typst", "compile", typst_input, pdf_output],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            with open(pdf_output, "rb") as f:
                pdf_data = f.read()
        except subprocess.CalledProcessError:
            pdf_data = b"Clearly not the typist I thought you were!\n"

    sys.stdout.buffer.write(pdf_data)


if __name__ == "__main__":
    main()
