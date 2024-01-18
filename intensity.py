# Intensity Level Slicing 

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

min_range = 150
max_range = 250  

with open ('images/1_intensity.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')
    
    for i in range(y):
        for j in range(x):
            a = 0
            if img1[i, j] > min_range and img1[i, j] < max_range:
                a = 255
            else:
                a = 0
            
            img.write("%s\n"%str(a))