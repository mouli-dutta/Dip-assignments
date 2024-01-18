import numpy as np
from PIL import Image


def sobel_operator(image):
    # Apply the Sobel operator to detect edges
    pixels = image.load()
    width, height = image.size
    new_image = Image.new("L", (width, height))
    new_pixels = new_image.load()

    for x in range(1, width - 1):
        for y in range(1, height - 1):
            gx = pixels[x + 1, y - 1] + 2 * pixels[x + 1, y] + pixels[x + 1, y + 1] - \
                 (pixels[x - 1, y - 1] + 2 * pixels[x - 1, y] + pixels[x - 1, y + 1])
            gy = pixels[x - 1, y + 1] + 2 * pixels[x, y + 1] + pixels[x + 1, y + 1] - \
                 (pixels[x - 1, y - 1] + 2 * pixels[x, y - 1] + pixels[x + 1, y - 1])
            gradient = int((gx**2 + gy**2)**0.5)
            new_pixels[x, y] = gradient

    return new_image

def threshold(image, threshold_value):
    # Apply a threshold to the image to create a binary image
    pixels = image.load()
    width, height = image.size
    binary_image = Image.new("L", (width, height))
    binary_pixels = binary_image.load()

    for x in range(width):
        for y in range(height):
            binary_pixels[x, y] = 255 if pixels[x, y] > threshold_value else 0

    return binary_image


f = open("scenari.pgm","r")
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


edges_image = sobel_operator(image)
binary_image = threshold(image, threshold_value=50)

g = open("line_detect.pgm","w")
g.write("%s" %p)
g.write("%s" %p1)
g.write("%s" %p2)
g.write("%s" %p3)

for i in range(h):
	for j in range(w):
		g.write("%d\n"%binary_image[i,j])
		
g.close()
