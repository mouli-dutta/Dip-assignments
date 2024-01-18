import numpy as np
import math

def convolve(image, kernel):
    height, width = image.shape
    k_height, k_width = kernel.shape
    h_pad = k_height // 2
    w_pad = k_width // 2

    result = np.zeros((height, width), dtype=np.float64)

    for i in range(h_pad, height - h_pad):
        for j in range(w_pad, width - w_pad):
            result[i, j] = np.sum(image[i - h_pad:i + h_pad + 1, j - w_pad:j + w_pad + 1] * kernel)

    return result

def vertical_line_detection(image):
    # Vertical Edge Detection Kernel
    kernel = np.array([[-1, 0, 1]])

    # Convolve the image with the vertical edge detection kernel
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

result_image = vertical_line_detection(image)

g = open("vertical.pgm","w")
g.write("%s" %p)
g.write("%s" %p1)
g.write("%s" %p2)
g.write("%s" %p3)

for i in range(h):
	for j in range(w):
		g.write("%d\n"%result_image[i,j])
		
g.close()

