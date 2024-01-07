from pwn import *
import itertools


"""
This is the intended solution.

You can pass the first level by passing the integer value of 0xdeadbeef.
For the second level by reverse engineering the binary you can get the array of numbers
needed to create a function that takes the number that the user inputs and xor's it with the array of numbers
until the xored number matches the number 505. The third and final level 
consist of guessing or rather bruteforcing the randomly generated number. 
When all these steps are combined in a script the flag will be read from the file flag.txt and printed to stdout.
"""

### Solve for level 1 ###
level_one = int(0xdeadbeef)
###########################


########### Solve for level 2 #################
def xor_num(num):
    xor_num_array = [55, 245, 138, 125, 258, 33]
    for i in range(0, len(xor_num_array)):
        num = num ^ xor_num_array[i]
        i += 1
    return num

i = 0
while True:
    if xor_num(i) == 505:
        level_two = str(i)
        break
    i += 1
##############################################



# p = process('./w1zArD')
p = remote('potluck.0xa.is', 31331)
p.sendline(str(level_one))
p.sendline(str(level_two))

######### Solve for level 3 ##################
numbers = '0123456789'
s = ''
for i in itertools.product(numbers, repeat=4):
    try:
        passcode = s + ''.join(i)
        p.sendline(passcode)
        print(p.recvline().decode('utf-8'))
    except EOFError:
        log.success("Done!")
        break
##############################################


