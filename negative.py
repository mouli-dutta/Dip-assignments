# Negative Transformation

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

img2 = max_int - img1

with open ('images/1_neg.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')

    img2 = img2.reshape(x * y)
    
    for i in range (x * y):
        img.write(str(img2[i]) + '\n')