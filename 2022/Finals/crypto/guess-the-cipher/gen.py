import yaml
LETTERS =  'abcdefghijklmnopqrstuvwxy'
def shift(x):
    if x not in LETTERS:
        return x
    return chr((3 * (ord(x) - ord('a'))) % 26 + ord('a'))

def encr(s):
    return ''.join(map(shift, s))

a = list(map(shift, LETTERS))
print(a)
print(len(set(a)) == len(a))

with open('gtc.txt', 'w') as f:
    f.write(encr(yaml.safe_load(open('meta.yml'))['flags']))
    f.write('\n')

