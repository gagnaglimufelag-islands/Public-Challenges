import requests

base_url = "https://www.boxentriq.com"
idx = 0

with open("./img_list") as f:
    for i in f:
        print(base_url + i[:-1])
        img = requests.get(base_url + i[:-1])

        print(img.__dict__)
        with open(f"imgs/{idx}", "wb") as img_f:
            img_f.write(img.content)

        idx = idx + 1
