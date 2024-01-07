from hashlib import sha256
from itertools import combinations

FILENAME = "letter.txt"
HASH = "565839d3cc494d5de7a69f3d1afe7626f6fd3a48fbb3c1d0a85f7fa83670ad3f"

# Two errors outside of flag, at most two left.
# By looking at the content of the file we can deduct that
# they are probably inside the flag, after the "?v=" and before the "}".
ERROR_BOUNDARIES = (204, 215)


def bruteforce_bit_flips(data, n):
    bit_positions = range((ERROR_BOUNDARIES[1] - ERROR_BOUNDARIES[0]) * 8)
    bits_to_flip = 1
    while bits_to_flip <= n:
        for pos in combinations(bit_positions, bits_to_flip):
            fixed_data = flip_bits(list(data), pos)
            if sha256(bytes(fixed_data)).digest().hex() == HASH:
                print("Solution found:\n")
                fixed_letter = bytes(fixed_data).decode()
                print(fixed_letter)
                print("\n\nThe flag:", fixed_letter[fixed_letter.find("10an{"):fixed_letter.find("}")+1])
                exit(0)
        bits_to_flip += 1


def flip_bits(byte_list, pos):
    start_pos = ERROR_BOUNDARIES[0]
    for p in pos:
        byte_pos = (p // 8) + start_pos
        bit_pos = 8 - (p % 8)
        byte_list[byte_pos] = (byte_list[byte_pos] ^ (1 << bit_pos)) & 0xFF
    return byte_list


def main():
    with open(FILENAME, "rb") as f:
        data = f.read()

    data = data.replace(b"\xa0", b" ", 1)  # Fix "I hope" error
    data = data.replace(b"6isit", b"visit", 1)  # Fix "visit" error

    bruteforce_bit_flips(data, 2)


if __name__ == "__main__":
    main()
