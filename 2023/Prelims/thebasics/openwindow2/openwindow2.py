def check(password):
    if len(password) != 64:
        print(len(password))
        return False

    correct_bytes = [
        99,
        48,
        110,
        103,
        3648 >> 5,
        52,
        116,
        117,
        108,
        97,
        116,
        49,
        48,
        110,
        115,
        33,
        49,
        33,
        49,
        33,
        49,
        33,
        95,
        110,
        48,
        119,
        95,
        117,
        95,
        107,
        110,
        48,
        119,
        95,
        120,
        48,
        114,
        95,
        110,
        48,
        119,
        95,
        117,
        114,
        95,
        114,
        51,
        52,
        100,
        121,
        95,
        116,
        111,
        95,
        98,
        51,
        95,
        97,
        95,
        114,
        51,
        118,
        101,
        114,
    ]
    pass_bytes = password.encode()
    result = [p ^ c for p, c in zip(pass_bytes, correct_bytes)]
    return all(b == 0 for b in result)


if __name__ == "__main__":
    password = input("Enter password: ")[3:-1]
    if check(password):
        print(f"gg{{{password}}}")
    else:
        print("You are going to have to try harder than that!")
