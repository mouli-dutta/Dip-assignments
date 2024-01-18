import numpy as np

def roberts_cross_operator(image):
    # Apply the Roberts Cross operator to detect edges
    height, width = image.shape
    new_image = np.zeros((height, width))

    for j in range(1, width):
        for i in range(1, height):
            gx = image[i, j] - image[i-1, j-1]
            gy = image[i-1, j] - image[i, j-1]
            gradient = float((gx**2 + gy**2)**0.5)
            new_image[i-1, j-1] = gradient

    return new_image

def threshold(image, threshold_value):
    # Apply a threshold to the image to create a binary image
    return (image > threshold_value).astype(int)

# Read PGM image
with open("image1.pgm", "r") as f:
    p = f.readline()
    p1 = f.readline()
    p2 = f.readline()
    p3 = f.readline()
    w, h = [int(i) for i in p2.split()]
    image = np.zeros((h, w), np.int64)

    for i in range(h):
        for j in range(w):
            image[i, j] = int(f.readline())

# Perform Roberts Cross edge detection
edges_image = roberts_cross_operator(image)
#binary_image = threshold(edges_image, threshold_value=50)

# Save the resulting edges image
with open("ROBERT_detect.pgm", "w") as g:
    g.write("%s" % p)
    g.write("%s" % p1)
    g.write("%s" % p2)
    g.write("%s" % p3)

    for i in range(h):
        for j in range(w):
            g.write("%d\n" % edges_image[i, j])
