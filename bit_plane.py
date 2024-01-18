# Bit Plane Slicing

import numpy as np

with open ('images/1.pgm', 'r') as img:
    word = img.readline()
    comment = img.readline()
    res = img.readline()
    max_int = int(img.readline())

    x, y = res.split(' ')
    x = int(x)
    y = int(y)

    img1 = []

    for i in range (x * y):
        img1.append(int(img.readline()))

    img1 = np.array(img1).reshape(y, x)

def bit_plane_slicing(image, bit_plane):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            flag = int(np.binary_repr(image[i, j], width = 8)[-bit_plane])
            if flag:
                image[i, j] = 255
            else:
                image[i, j] = 0

    return image

def get_bit_plane(image, bit):
    bit_plane = (image >> bit) & 1
    return bit_plane * 255

bit_plane = 7
img2 = get_bit_plane(img1, bit_plane)


with open (f'images/1_{bit_plane}_bit_plane.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')

    img2 = img2.reshape(x * y)
    
    for i in range (x * y):
        img.write(str(img2[i]) + '\n')