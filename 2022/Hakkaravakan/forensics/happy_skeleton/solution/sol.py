import sys
import cv2
import zlib

PNG_HEADER = b'\x89PNG\r\n\x1a\n'

filename = sys.argv[1]
file = open(filename,'rb').read()

def i2b(a,pad=4):
    return bytes.fromhex(hex(a)[2:].zfill(pad*2))


crc = file[12+4+13:12+4+13+4]

for width in range(1000):
    for height in range(1000):
        ihdr = b'IHDR' + i2b(width) + i2b(height)+file[24:12+4+13]
        if i2b(zlib.crc32(ihdr)) == crc: 
            print("FOUND")
            open("/tmp/flag.png",'wb').write(PNG_HEADER +i2b(13) + ihdr+file[12+4+13:])
            break

