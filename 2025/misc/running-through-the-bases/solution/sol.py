import base64

with open("src/flag.enc") as f:
    output = f.read().encode()

while True:
    tmp = output.decode().split(",")

    if len(tmp) <= 1:
        break

    if tmp[1] == "16":
        output = base64.b16decode(tmp[0].encode())
    elif tmp[1] == "32":
        output = base64.b32decode(tmp[0].encode())
    elif tmp[1] == "64":
        output = base64.b64decode(tmp[0].encode())
    elif tmp[1] == "85":
        output = base64.b85decode(tmp[0].encode())

print(output)