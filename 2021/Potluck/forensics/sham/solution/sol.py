#!/usr/bin/python3

import zipfile, itertools, subprocess, sys, os, zwsp_steg

"""
Intended solution:

Doing basic forensics on the image file (ex: binwalk)
reveals a hidden zip file. Upon further inspection
you see that the zip file is password protected.


Going back and looking at the 'work-note.txt' file
in a hexdump you can see that there are
a bunch of seemingly empty lines.

Upon inspecting the bytes or the unicode chars
you get to know that these bytes or characters are called zero-width characters,
zero-width non-joiner, zero-width joiner and zero-width space.

using a zero-width decoder reveals another message
and in that message is a hint for the zip file password.

With the hint in mind you can craft a zip file password cracker
that runs through the combination 0000-9999.

After the cracker tries the combination 7564
it will extract the contents of the zip file
which includes a message and the flag.

10an{23r0_W1d7h_53cUR3_3ncRyP710N}
"""


# Check if user has supplied an image
if len(sys.argv) == 2:
    pass
else:
    print("Usage: ./solve.py <image.jpg>")
    exit(0)

#################################################### STAGE 1 ############################################################################


# Read the contents of work-note.txt
# Decode the zero-width message and write the gathered data to a file called 'private-message.txt'

with open("work-note.txt", "r") as f:
    data = f.read()

decode = zwsp_steg.decode(data)
with open("private-message.txt", "a") as f:
    f.write("[+] Public Message\n\n")
    f.write(data)
    f.write("\n[+] Private Message\n\n")
    f.write(decode)
    f.write("\n\n")






#################################################### STAGE 2 ############################################################################


# Create variables that hold the full paths to specific data
extracted_dir = os.getcwd() + '/' + '_{}.extracted/'.format(str(sys.argv[1])) # The directory that the zip file is at
secret_file = os.getcwd() + '/' + '_{}.extracted/'.format(str(sys.argv[1])) + 'secret.txt' # Point to the secret.txt file


# Extract data from the given image and remove the empty note.txt file
subprocess.run(['binwalk', '-eq', str(sys.argv[1])]) # Extract all data
subprocess.run(['rm', secret_file]) # Remove the empty secret.txt file



# Start cracking the zip file passcode
zip_file = extracted_dir + 'D576.zip'
zip_file = zipfile.ZipFile(zip_file)

numbers = '0123456789'
s = ''

for i in itertools.product(numbers, repeat=4):
    try:
        passcode = s + ''.join(i)
        zip_file.extractall(pwd=str.encode(passcode), path=extracted_dir)
    except:
        continue

    else:
        break

# Read from the not so empty secret.txt file
with open(secret_file, "r") as f:
    data = f.read()
print("\n",data)


# Clean up
subprocess.run(['rm', '-rf', extracted_dir]) # Remove the binwalk extracted directory
