import string
import yaml

UPPER = string.ascii_uppercase
N = len(UPPER)

FLAG = yaml.load(open('meta.yml'), Loader=yaml.Loader)['flags'][0]['flag']
MESSAGE = FLAG
SHIFT = 17

def lmap(letter):
    letter = letter.upper()
    if letter in UPPER:
        return UPPER[(UPPER.index(letter) + SHIFT) % N]
    return letter

def main():
    s = MESSAGE.upper()
    print(''.join(map(lmap, s)))


main()
