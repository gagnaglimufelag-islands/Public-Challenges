import yaml
import logging
from pwn import log
from pathlib import Path

logger = logging.getLogger("secretary")


# Load the flag dynamically from the meta file
HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

def test():
    try:
        import angr
    except ImportError:
        print("Error Importing 'angr'")
        exit(0)
    proj = angr.Project(str(HERE / 'chal' / "angry"))
    simgr = proj.factory.simgr()
    simgr.explore(find=lambda s: b"\n[+] YOU GOT THE FLAG!\n\n" in s.posix.dumps(1))
    flag = simgr.found[0].posix.dumps(0).decode()
    log.success(flag)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    test()
