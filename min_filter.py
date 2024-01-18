# Min filter

import numpy as np

with open ('images/3.pgm', 'r') as img:
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

img2 = np.zeros((y, x), int)
            
for i in range(1, y - 1):
    for j in range(1, x - 1):
        img2[i, j] = min(img1[i - 1, j - 1], img1[i, j - 1], img1[i + 1, j -1], img1[i - 1, j], img1[i, j], img1[i + 1, j], img1[i - 1, j + 1], img1[i, j + 1], img1[i + 1, j + 1])

with open ('images/3_min.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')

    img2 = img2.reshape(x * y)
    
    for i in range (x * y):
        img.write(str(img2[i]) + '\n')