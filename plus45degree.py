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

def plus_45_degree_line_detection(image):
    # Plus 45-degree Edge Detection Kernel
    kernel = np.array([[-1, -1, 2], [-1, 2, -1], [2, -1, -1]])

    # Convolve the image with the plus 45-degree edge detection kernel
    result = convolve(image, kernel)

    # Thresholding to highlight edges
    threshold = 50
    result[result > threshold] = 255
    result[result <= threshold] = 0

    return result.astype(np.uint8)

f = open("images.pgm","r")
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

# Example usage
 #image = np.random.randint(0, 256, size=(10, 10), dtype=np.uint8)  # Replace this with your image data

result_image = plus_45_degree_line_detection(image)

g = open("plus45degree.pgm","w")
g.write("%s" %p)
g.write("%s" %p1)
g.write("%s" %p2)
g.write("%s" %p3)

for i in range(h):
	for j in range(w):
		g.write("%d\n"%result_image[i,j])
		
g.close()

