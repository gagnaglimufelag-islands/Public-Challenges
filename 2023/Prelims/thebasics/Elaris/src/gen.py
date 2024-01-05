#!/usr/bin/env python3

from PIL import Image

def encode_lsb(input_image, output_image, message):
    flag = "gg{" + message + "}"
    flag_bits = ''.join(format(ord(i), '08b') for i in flag)

    img = Image.open(input_image)
    width, height = img.size
    img_data = list(img.getdata())

    if len(flag_bits) > width:
        raise ValueError("The flag is too long for the given image width")

    new_img_data = []
    for y in range(height):
        for x in range(width):
            i = y * width + x
            r, g, b, a = img_data[i]
            if y == 0 and x < len(flag_bits):
                b = (b & 0b11111110) | int(flag_bits[x])
            new_pixel = (r, g, b, a)
            new_img_data.append(new_pixel)

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_img_data)
    new_img.save(output_image)

encode_lsb("input.png", "Map.png", "Find_the_tree_that_whispers_secrets_and_the_island_lies_where_its_roots_converge")
