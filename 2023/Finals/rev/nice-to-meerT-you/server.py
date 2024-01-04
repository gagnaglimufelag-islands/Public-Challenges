import os

FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")

def valid_key(key):
    words = key.split("_")
    if len(words) != 10:
        return False

    for word in words[1::]:
        if word == words[0]:
            return False

    for word in words:
        if word != "".join(sorted(word)):
            return False
        if len(word) < 5:
            return False

    return True

key = input("Enter key: ")
if valid_key(key):
    print(f"Correct!\n{FLAG}")
else:
    print("Nope!")
