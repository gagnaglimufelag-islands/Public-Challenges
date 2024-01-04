import zlib
import cv2
import struct
import yaml
from pathlib import Path 
from base64 import b64encode


HERE = Path(__file__).parent
FLAG = yaml.safe_load(open(HERE / "meta.yml"))["flags"].encode()

flag_bits = bin(int.from_bytes(FLAG, 'big'))[2:].zfill(len(FLAG)*8)

HEADER = b'\x89PNG\r\n\x1a\n'


def get_checksum(chunk_type: bytes, data: bytes) -> int:
	return zlib.crc32(chunk_type + data)

def chunk(chunk_type: bytes, data: bytes) -> None:
	out = struct.pack('>I', len(data))
	out += chunk_type
	out += data

	checksum = get_checksum(chunk_type, data)
	out += struct.pack('>I', checksum)
	return out

def make_ihdr(width: int, height: int, bit_depth: int, color_type: int) -> bytes:
	return struct.pack('>2I5B', width, height, bit_depth, color_type, 0, 0, 0)

def encode_data(img):
	out = []
	
	for row in img:
		out += [0]
		for pixel in row:
			values = [cv for cv in pixel]
			out.extend(values)
	return out

def compress(data):
	return zlib.compress(bytearray(data))

def dump_png(img) -> None:
	out = bytearray(HEADER)

	assert len(img) > 0 
	width = len(img[0])
	height = len(img)
	bit_depth = 8  # bits per pixel
	color_type = 2  # pixel is RGB triple

	ihdr_data = make_ihdr(width, height, bit_depth, color_type)
	out += chunk(b'IHDR', ihdr_data)
	
	x=100
	encoded = compress(encode_data(img))
	'''
	out += chunk(b'IDAT', data=encoded[:x])
	out += chunk(b'IDAT', data=encoded[x:])
	'''
	one = 10
	zero = 20
	normal = 10
	for c in flag_bits:
		if c == '1':
			out += chunk(b'IDAT', data=(encoded[:one]))
			encoded = encoded[one:]
		else:
			out += chunk(b'IDAT', data=(encoded[:zero]))
			encoded = encoded[zero:]
	while len(encoded) != 0:
		out += chunk(b'IDAT', data=(encoded[:normal]))	
		encoded = encoded[normal:]

	out += chunk(b'IEND', data=b'')
	return out

def save_png(img, filename: str) -> None:
	img = dump_png(img)
	with open(filename, 'wb') as out:
		out.write(img)


img = cv2.imread("hax.png", cv2.IMREAD_COLOR)
save_png(img, 'files/chall.png')
