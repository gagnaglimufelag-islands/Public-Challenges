def check(password):
    if len(password) % 2 != 0:
        return False

    end = len(password) - 1
    for start in range(len(password) // 2):
        password[start], password[end] = password[end], password[start]
        end -= 1
    return "".join(password) == "0o0r4hct1wsl03ht"


if __name__ == "__main__":
    password = input("Enter password: ")[3:-1]
    if check(list(password)):
        print(f"gg{{{password}}}")
    else:
        print("You are going to have to try harder than that!")
