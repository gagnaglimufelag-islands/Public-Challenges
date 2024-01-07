p = 27046780809278300597
g = Mod(2, p)

ct = Mod(int(input('Enter ciphertext: ')), p)

secret = discrete_log(ct, g)
print('secret: {}'.format(secret))
