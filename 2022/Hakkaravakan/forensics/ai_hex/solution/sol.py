import yaml
import logging
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

logger = logging.getLogger("secretary")


def test():
    flag = []
    data = open(HERE / "./Secret_codes-An_AI_story.pdf", "rb").readlines()[-29:]
    data_index = 0
    flag_index = 0

    while flag_index < len(FLAG):
        flag.append(
            chr(data[data_index][data[data_index].find(FLAG[flag_index].encode())])
        )
        if chr(data[data_index][-2]) != " ":
            flag.append(chr(data[data_index][-2]))
            flag_index += 1
        flag_index += 1
        data_index += 1

    flag = "".join(flag)
    assert FLAG in flag, flag


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    test()
