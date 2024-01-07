import cv2
import zlib

img = cv2.imread('skeleton.png')

with open('flag.txt') as f:
    flag = f.read()[:-1]
print(flag.encode())
cv2.putText(img=img, text=flag, org=(40,500), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=0.8, color=(255,255,255),thickness=2)

cv2.imshow("img",img)
cv2.waitKey(0) 

cv2.imwrite("files/skeleton.png",img)

file = open("files/skeleton.png",'rb').read()

def i2b(a,pad=4):
    return bytes.fromhex(hex(a)[2:].zfill(pad*2))

index = 16
width = int.from_bytes(file[index:index+4],"big")
print(width)
index += 4
height = int.from_bytes(file[index:index+4],"big")
print(height)

chall = b'\xff'*24 + file[24:]
open("files/skeleton.png","wb").write(chall)


print((file[12+4+13:12+4+13+4]))
print(i2b(zlib.crc32(file[12:12+4+13])))



