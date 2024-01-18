# Global Thresholding

import numpy as np
import random

with open ('images/5.pgm', 'r') as img:
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

def global_thershold(image, dT):
    T = random.randint(0, 255)
    T_new = 0

    while(abs(T - T_new) > dT):
        T = T_new
        g1 = image[image > T]
        g2 = image[image <= T]

        if len(g1) == 0:
            m1 = 0
        else:
            m1 = np.mean(g1)

        if len(g2) == 0:
            m2 = 0
        else:
            m2 = np.mean(g2)

        T_new = (m1 + m2) / 2

    return T_new

img1[img1 > global_thershold(img1, 0)] = 255
img1[img1 <= global_thershold(img1, 0)] = 0

with open ('images/5_input.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')

    img1 = img1.reshape(x * y)
    
    for i in range (x * y):
        img.write(str(img1[i]) + '\n')