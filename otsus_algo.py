import numpy as np
import random

with open('images/1.pgm', 'r') as img:
    word = img.readline()
    comment = img.readline()
    res = img.readline()
    max_int = int(img.readline())

    x, y = res.split(' ')
    x = int(x)
    y = int(y)

    img1 = []

    for i in range(x * y):
        img1.append(int(img.readline()))

    img1 = np.array(img1).reshape(y, x)

def between_class_var(image, k):
    unique, count = np.unique(image, return_counts=True)
    res = image.shape[0] * image.shape[1]
    p = count / res
    P1 = np.sum(p[:k])
    P2 = 1 - P1

    sum1 = 0
    for i in range(k):
        sum1 += i * p[i]

    m1 = sum1 / P1

    sum2 = 0
    for i in range(k, len(p)):
        sum2 += i * p[i]

    m2 = sum2 / P2

    mg = (P1 * m1) + (P2 * m2)

    # global_var = 0
    # for i in range(len(p)):
    #     global_var += ((i - mg) ** 2) * p[i]

    var = P1 * (m1 - mg) + P2 * (m2 - mg)

    return var

def otsu_threshold(image):
    T = np.arange(0, 256)

    var_list = []

    for intensity in T:
        var_list.append(between_class_var(image, intensity))

    threshold = np.argmax(var_list)

    # between_class_var = P1 * P2 * (m1 - m2) # Another formula

    return threshold

# Assuming img1 is the image you want to apply Otsu's method to
threshold_value = otsu_threshold(img1)

# Apply the threshold to the image
img3 = np.where(img1 > threshold_value, max_int, 0)

# Write the result to a new PGM file
with open('images/otsu_applied.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')

    img3 = img3.reshape(x * y)

    for i in range(x * y):
        img.write(str(img3[i]) + '\n')
