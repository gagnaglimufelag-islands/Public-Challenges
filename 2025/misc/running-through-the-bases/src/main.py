import base64

flag = "gg{wow_you_sure_know_how_to_run}".encode()
encode_list = [64, 32, 16, 85, 64, 64, 32, 85, 64, 16, 16, 32, 64, 16, 64, 64, 85, 64]
output = flag

for i in encode_list:
    if i == 16:
        tmp = base64.b16encode(output)
        output = f"{tmp.decode()},16".encode()
    elif i == 32:
        tmp = base64.b32encode(output)
        output = f"{tmp.decode()},32".encode()
    elif i == 64:
        tmp = base64.b64encode(output)
        output = f"{tmp.decode()},64".encode()
    elif i == 85:
        tmp = base64.b85encode(output)
        output = f"{tmp.decode()},85".encode()


print(output)
