#contrast Stretching

import numpy as np

with open ('images/2.pgm', 'r') as img:
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
            
max = np.max(img1)
min = np.min(img1)

for i in range(y):
    for j in range(x):
        img1[i, j] = int(max_int) * (img1[i, j] - min) / (max - min)
        
with open ('images/2_contrast.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')

    img1 = img1.reshape(x * y)
    
    for i in range (x * y):
        img.write(str(img1[i]) + '\n')
