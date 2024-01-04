#!/usr/bin/env python3
import os
import io
import re
import random
from math import ceil
from base64 import b64encode
import cv2
import numpy as np
from PIL import Image

WIDTH = 32
HEIGHT = 32
MAX_INDEX = 127
IS_THIS_LOSS = "./isthisloss.png"
INPUT_RE = r"([0-9]{1,3}), ?([0-9]{1,3})"
FLAG = os.environ.get("FLAG", "falg{NotYourFlag}")
MESSAGES = [
    "IMAGINARY ENEMY WHO I PRETEND IS MY FRIEND TO MESS WITH THEIR HEAD!",
    "REFLECTION IN A WINDOW THAT I'VE BEEN WAVING TO FOR HOURS!",
    "SHADOW THAT I MISTOOK FOR A PERSON BECAUSE I'M EASILY SPOOKED!",
    "CAT WHO I DRESS UP IN HUMAN CLOTHES AND CALL MY FRIEND!",
    "PLANT WHO I TALK TO BECAUSE IT'S A GOOD LISTENER!",
    "SOCK PUPPET WHO I USE TO PRACTICE MY VENTRILOQUISM!",
    "ALTERNATE UNIVERSE VERSION OF MYSELF WHO'S HERE TO WARN ME ABOUT SOMETHING!",
    "FIGMENT OF MY IMAGINATION THAT I'M TOO EMBARRASSED TO ADMIT TO!",
    "ROBOT COMPANION WHO I PROGRAMMED TO ACT LIKE MY FRIEND!",
    "LONG LOST TWIN WHO WAS SEPARATED FROM ME AT BIRTH!",
    "EVIL TWIN WHO'S BEEN IMPERSONATING ME THIS WHOLE TIME!",
    "PET ROCK THAT I PAINTED A FACE ON!",
    "REFLECTION IN A FUNHOUSE MIRROR THAT CAME TO LIFE!",
    "TIME-TRAVELING FUTURE SELF WHO FORGOT TO TELL ME ABOUT THIS ENCOUNTER!",
    "CLONE WHO I ACCIDENTALLY CREATED IN MY SCIENCE EXPERIMENT!",
    "ALTER EGO WHO ONLY COMES OUT ON TUESDAYS!",
    "UNDERCOVER SPY WHO'S BEEN MONITORING MY EVERY MOVE!",
]


def random_index():
    return (random.randint(0, MAX_INDEX), random.randint(0, MAX_INDEX))


def create_pos(x, y):
    start_x = x * WIDTH
    start_y = y * HEIGHT
    end_x = start_x + WIDTH
    end_y = start_y + HEIGHT
    return (start_x, start_y, end_x, end_y)


def crop_image(pos):
    friend = io.BytesIO()
    crop = Image.open(IS_THIS_LOSS).crop(pos)
    crop.save(friend, format="PNG")
    return friend.getvalue()


def find_pos(friend):
    loss = cv2.imread(IS_THIS_LOSS)
    nparr = np.frombuffer(friend, np.uint8)
    find = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(loss, find, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    locs = np.where(res >= threshold)
    for pt in zip(*locs[::-1]):
        return pt  # Only need the first one


def get_and_parse_ans():
    while True:
        ans = input("> ")
        m = re.match(INPUT_RE, ans)
        if m is None:
            print("Invalid input!")
            continue
        return (int(m.group(1)), int(m.group(2)))

def same_pos(left, right):
    return all(a == b for a, b in zip(left, right))

def generate_friend():
    while True:
        (c_x, c_y) = random_index()
        pos = create_pos(c_x, c_y)
        friend = crop_image(pos)
        (f_x, f_y) = find_pos(friend)
        found = (ceil(f_x / WIDTH), ceil(f_y / HEIGHT))
        if not same_pos((c_x, c_y), found):
            continue
        elif same_pos((0, 4), found):
            return ((0, 4), friend)
        return ((c_x, c_y), friend)


print("============================")
print("#      Help me             #")
print("#         find my          #")
print("#            friends!      #")
print("============================")
print(f"Answers should match: {INPUT_RE}")
print()

for i in range(5):
    (correct, friend) = generate_friend()
    print(f"Friend #{i + 1}")
    print(f"profile pic: {b64encode(friend).decode()}")
    print("Where is my friend?")
    ans = get_and_parse_ans()
    if all(a == b for a, b in zip(ans, correct)):
        print("Correct!")
        if i < 4:
            print("Generating next friend...\n")
    else:
        print(f"WRONG! THAT IS NOT MY FRIEND BUT MY {random.choice(MESSAGES)}")
        exit(1)

print(
    f"Woo! You found all my internet friends who I've never actually met in person! Here is the flag: {FLAG}"
)
