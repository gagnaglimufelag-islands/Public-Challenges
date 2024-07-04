import math
import os
import random

# Directions
#       3
#       N
#  2 W     E 0
#       S
#       1

fake_proverbs = [
    "Do not drink and park; accidents cause people.",
    "A wise man once said nothing, then walked away with everyone's sandwiches.",
    "He who laughs last, didn't get the joke.",
    "A bird in hand is worth two in the bush, but still not enough for a good meal.",
    "An apple a day keeps anyone away, if thrown hard enough.",
    "Even a broken clock is right twice a day, but it’s also annoying all the time.",
    "The early bird catches the worm, but the second mouse gets the cheese.",
    "If at first you don't succeed, destroy all evidence that you tried.",
    "He who throws dirt is losing ground.",
    "When in doubt, mumble. When in trouble, delegate.",
    "The journey of a thousand miles begins with a single step, and a really good playlist.",
    "Do not take life too seriously. You will never get out of it alive.",
    "A closed mouth gathers no foot.",
    "The pen is mightier than the sword, but a sword is much pointier.",
    "Man who runs in front of car gets tired. Man who runs behind car gets exhausted.",
    "Confucius say: Man who stands on toilet is high on pot.",
    "Wise man always knows banana is best when brown spots appear.",
    "He who fishes in another man's pond often catches crabs.",
    "It takes many nails to build a crib, but only one screw to fill it.",
    "The squeaky wheel gets annoying fast.",
    "When life gives you lemons, squirt someone in the eye.",
    "A clear conscience is usually a sign of a bad memory.",
    "The road to success is always under construction.",
    "If you think nobody cares if you’re alive, try missing a couple of car payments.",
    "A truly wise man never plays leapfrog with a unicorn.",
    "Better to remain silent and be thought a fool than to speak out and remove all doubt.",
    "If you can't convince them, confuse them.",
    "Time flies like an arrow; fruit flies like a banana.",
    "A conclusion is the place where you got tired of thinking.",
    "He who laughs last thinks slowest.",
    "The early bird gets the worm, but the second mouse gets to sleep in.",
    "A penny saved is ridiculous.",
    "Many hands make light work, unless they are all thumbs.",
    "A journey of a thousand miles begins with a cash advance.",
    "A problem shared is a problem halved, but so is the praise.",
    "Don’t put all your eggs in one basket; it makes juggling easier.",
    "A day without sunshine is like, you know, night.",
    "Even a stopped clock is right twice a day. But you wouldn’t want to cook dinner by it.",
    "The grass is always greener on the other side, but that's because they use more fertilizer.",
    "When the cat’s away, the mice will mess up your Wi-Fi.",
    "If the shoe fits, buy it in every color.",
    "Too many cooks spoil the broth, but they make a fantastic potluck.",
    "Never test the depth of the water with both feet.",
    "He who stands on a pedestal has nowhere to step but off.",
    "Wisdom comes with age, but sometimes age comes alone.",
    "If you want to catch a squirrel, climb a tree and act like a nut.",
    "Two wrongs don't make a right, but three lefts do.",
    "To err is human; to blame it on someone else shows management potential.",
    "He who drinks a fifth on the fourth may not go forth on the fifth."
]

FLAG = os.getenv('FLAG', f'99{{{"".join(chr(97+i) for i in range(21))}}}')

def advance(coord, sp, d):
    new = list(coord)
    if d == 0:
        new[1] += 1
    if d == 1:
        new[0] += 1
    if d == 2:
        new[1] -= 1
    if d == 3:
        new[0] -= 1

    try:
        if sp[new[0]][new[1]] != 0:
            raise IndexError()
        return d, tuple(new)
    except IndexError:
        return advance(coord, sp, (d+1)%4)


def spiral(text):
    n = int(math.sqrt(len(text)))
    sp = [ [0 for _ in range(n)] for __ in range(n)]
    d = 0
    coord = (0,0)
    printed = text[:n**2]
    queue = list(printed)
    while queue:
        sp[coord[0]][coord[1]] = queue.pop(0)
        if queue:
            d, coord = advance(coord, sp, d)

    return '\n'.join(map(''.join,sp))


def riddle(text):
    n = int(math.sqrt(len(text)))
    printed = text[:n**2]
    print('----')
    print(spiral(text))
    print('----')
    ans = input('Answer: ').strip()
    if ans.startswith(printed.rstrip('X')):
        print('You got that one!')
    else:
        print("Nope, that doesn't seem to match")
        exit(1)




def welcome():
    print('''.▄▄ ·  ▄▄▄·▪  ▄▄▄   ▄▄▄· ▄▄▌   ▄▄ •       ▄▄▄  ▪  ▄▄▄▄▄ ▄ .▄• ▌ ▄ ·. 
▐█ ▀. ▐█ ▄███ ▀▄ █·▐█ ▀█ ██•  ▐█ ▀ ▪▪     ▀▄ █·██ •██  ██▪▐█·██ ▐███▪
▄▀▀▀█▄ ██▀·▐█·▐▀▀▄ ▄█▀▀█ ██▪  ▄█ ▀█▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█.▪██▀▐█▐█ ▌▐▌▐█·
▐█▄▪▐█▐█▪·•▐█▌▐█•█▌▐█ ▪▐▌▐█▌▐▌▐█▄▪▐█▐█▌.▐▌▐█•█▌▐█▌ ▐█▌·██▌▐▀██ ██▌▐█▌
 ▀▀▀▀ .▀   ▀▀▀.▀  ▀ ▀  ▀ .▀▀▀ ·▀▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀ ▀▀▀ ▀▀▀ ·▀▀  █▪▀▀▀

''')
    print('You have found the mysterious server of Spiralgorithm.')
    print('I have 30 ancient runestones that contain hidden messages. Can you decipher them?')
    print()


def main():
    welcome()
    random.shuffle(fake_proverbs)
    for i, prov in enumerate(fake_proverbs[:30]):
        print(f'Mystery {i+1}')
        fixed = prov.replace(' ', '_')
        dim = int(math.sqrt(len(fixed)))
        if dim ** 2 != len(fixed):
            fixed = fixed + ((dim+1)**2 - len(fixed)) * 'X'
        riddle(fixed)

    print('You are a regular riddle solver, you can have the flag but you have to work for it')
    print('----')
    print(spiral(FLAG))
    print('----')

if __name__ == '__main__':
    main()
