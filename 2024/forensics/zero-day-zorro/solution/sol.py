import yaml
from pathlib import Path

HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]
def test():
    lines = [x for x in open('access.log').read().splitlines() if 'Query performance of' in x]
    times = [float(x.split()[-2]) for x in lines]

    found = []
    while True:
        chunk = times[-8:]
        times = times[:-8]

        l, r = 0, 255
        for t in chunk:
            m = (l + r) // 2
            if t > 0.1:
                l = m + 1
            else:
                r = m

        found.append(chr(r))
        if found[-2:] == list('gg'):
            break

    flag = ''.join(found[::-1])
    assert FLAG == flag
