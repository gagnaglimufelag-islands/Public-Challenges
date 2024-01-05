alphabet_mapping = {
    "А": "a",
    "Б": "b",
    "В": "v",
    "Г": "g",
    "Д": "d",
    "Е": "ye",
    "Ё": "yo",
    "Ж": "zh",
    "З": "z",
    "И": "i",
    "Й": "y",
    "К": "k",
    "Л": "l",
    "М": "m",
    "Н": "n",
    "О": "o",
    "П": "p",
    "Р": "r",
    "С": "s",
    "Т": "t",
    "У": "u",
    "Ф": "f",
    "Х": "kh",
    "Ц": "ts",
    "Ч": "ch",
    "Ш": "sh",
    "Щ": "shch",
    "Ъ": '"',
    "Ы": "y",
    "Ь": "'",
    "Э": "e",
    "Ю": "yu",
    "Я": "ya",
}


def rot_n(msg, n):
    alphabet = list(alphabet_mapping)
    cipher = []

    for char in msg:
        if char not in alphabet:
            cipher.append(char)
            continue

        cipher.append(alphabet[(alphabet.index(char) + n) % len(alphabet)])

    return "".join(cipher)


def translate(rus):
    eng = []
    for char in rus:
        if char not in alphabet_mapping:
            eng.append(char)
            continue

        eng.append(alphabet_mapping[char])

    return "".join(eng)


rus_flag = "ЁУ_ГУЭССЭД_ТЭ_ЧИФЭР"
eng_flag = translate(rus_flag)
cipher = rot_n(rus_flag, 13)

assert rus_flag == rot_n(cipher, -13)
assert eng_flag == translate(rot_n(cipher, -13))

print("Tests passed!")
print(f"Rus Flag: {rus_flag}")
print(f"Real Flag: {eng_flag}")

with open("wat.txt", "w") as f:
    f.write(cipher)
