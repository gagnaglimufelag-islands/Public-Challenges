import string

with open("./t.txt") as f:
    s = f.read().rstrip()

m = {" ": "_", "a": "4", "i": "1", "e": "3", "g": "6", "s": "5", "t": "7", "z": "2"}

for k in m:
    s = s.replace(k, m[k])

l = 32
arr = []
i = l
j = 0

while True:
    if i > len(s):
        break
    arr.append("{'" + "', '".join(s[j:i]) + "'}")
    j = i
    i += l

arr.append("{'" + "', '".join(s[j:i]) + "', " + "'_', " * (l - len(s[j:i]) - 1) + "'_'}")

print(",\n".join(arr))

print(len(arr))
