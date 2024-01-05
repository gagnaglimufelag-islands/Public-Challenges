import yaml
import logging
from pathlib import Path


logger = logging.getLogger("secretary")


# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

    
### IF STANDALONE (i.e. work on chall.txt) ###
def test():
    with open("flag.txt", "r") as f:
        data = f.read()
    binary_string = ''.join(['1' if x == '👍' else '0' for x in data])
    chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    flag = ''.join([chr(int(chunk, 2)) for chunk in chunks])
    logger.debug(flag)
    assert FLAG in flag, flag

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    test()
