from pathlib import Path
import logging
import factor
import re
import yaml

logger = logging.getLogger("secretary")

# For OOB interaction, if required
OAST = re.compile(r"\[.*INF.*\] ([a-z0-9]+\.[a-z0-9]+\.[a-z]+)")

# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]



def test():
    with open("files/out.txt", "r") as f:
        out = f.read()

    n = int(out.split('\n')[0])
    e = 0x10001

    p_out = out.split('\n')[1].replace('?','_')
    q_out = out.split('\n')[2].replace('?','_')

    enc = int(out.split('\n')[3],16)

    p,q = factor.from_str(n, p_out, q_out)
    assert p*q == n

    phi = (p-1)*(q-1)
    d = pow(e, -1 , phi)
    flag = bytes.fromhex(hex(pow(enc, d, n))[2:]).decode()


    assert FLAG in flag, flag


if __name__ == "__main__":
    test()
