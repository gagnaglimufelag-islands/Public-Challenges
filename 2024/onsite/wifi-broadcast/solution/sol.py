import re
from pathlib import Path
import subprocess

HERE = Path(__file__).parent


def test():
    decoded = ""
    with open(HERE / "src" / "broadcast.py", "r") as f:
        match = re.search(r"gg\{.*\}", f.read())
        assert match is not None

        command = 'tshark -r cap.pcapng -Y "udp.port == 50050" -T fields -e data'
        result = subprocess.check_output(command, shell=True, text=True).split("\n")[:-1]

        decoded = {}
        for i in result:
            line = bytes.fromhex(i).decode('utf-8').split(" ")

            idx = int(line[0])
            val = line[1]

            decoded[idx] = val

        sorted_keys = [*decoded.keys()]
        sorted_keys.sort()
        
        flag = ""
        for i in sorted_keys:
            flag += decoded[i]
        
        assert flag is not None

    assert match[0] == flag


if __name__ == "__main__":
    test()
