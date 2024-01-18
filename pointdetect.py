import numpy as np
import math


def convolve(image, kernel):
    height, width = image.shape
    k_size = len(kernel)
    pad_size = k_size // 2

    result = np.zeros((height, width), dtype=np.float64)

    for i in range(pad_size, height - pad_size):
        for j in range(pad_size, width - pad_size):
            result[i, j] = np.sum(image[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1] * kernel)

    return result

def point_detection(image):
    # Laplacian Kernel for Edge Detection
    kernel = np.array([[1, 1, 1],
                       [1, -8, 1],
                       [1, 1, 1]])

    # Convolve the image with the Laplacian kernel
    result = convolve(image, kernel)

    # Thresholding to highlight edges
    threshold = 50
    result[result > threshold] = 255
    result[result <= threshold] = 0

    return result.astype(np.uint8)

f = open("pointimage.pgm","r")
p = f.readline()
p1 = f.readline()
p2 = f.readline()
p3 = f.readline()
w, h = [int(i) for i in p2.split()]
image = np.zeros((h,w), np.int64)

for i in range(h):
	for j in range(w):
		image[i,j]=int(f.readline())
		
f.close



result_image = point_detection(image)

g = open("pointdetect.pgm","w")
g.write("%s" %p)
g.write("%s" %p1)
g.write("%s" %p2)
g.write("%s" %p3)

for i in range(h):
	for j in range(w):
		g.write("%d\n"%result_image[i,j])
		
g.close()
