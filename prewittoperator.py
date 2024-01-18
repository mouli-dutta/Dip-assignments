import numpy as np

def prewitt_operator(image):
    # Apply the Prewitt operator to detect edges
    height, width = image.shape
    new_image = np.zeros((height, width))

    for i in range(1, height-1):
        for j in range(1, width-1):
            # Prewitt kernels
            dx = image[i-1, j+1] + image[i, j+1] + image[i+1, j+1] - (image[i-1, j-1] + image[i, j-1] + image[i+1, j-1])
            dy = image[i-1, j-1] + image[i-1, j] + image[i-1, j+1] - (image[i+1, j-1] + image[i+1, j] + image[i+1, j+1])

            gradient_magnitude = int((dx**2 + dy**2)**0.5)
            new_image[i-1, j-1] = gradient_magnitude

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
edges_image = prewitt_operator(image)
#binary_image = threshold(edges_image, threshold_value=50)

# Save the resulting edges image
with open("PREWITT_edge_detect.pgm", "w") as g:
    g.write("%s" % p)
    g.write("%s" % p1)
    g.write("%s" % p2)
    g.write("%s" % p3)

    for i in range(h):
        for j in range(w):
            g.write("%d\n" % edges_image[i, j])
