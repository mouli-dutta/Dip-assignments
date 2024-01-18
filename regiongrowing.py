import numpy as np

def region_growing(image, seed_points, threshold=0.1):
    """Performs region growing from given seed points.

    Args:
        image: A grayscale image as a NumPy array.
        seed_points: A list of (y, x) coordinates for seed points.
        threshold: The maximum intensity difference allowed for region growing (default: 0.1).

    Returns:
        A NumPy array representing the segmented image, where each region has a unique integer label.
    """

    segmented_image = np.zeros_like(image, dtype=int)  # Stores region labels
    region_label = 1

    for y, x in seed_points:
        if segmented_image[y, x] == 0:  # Only grow from unassigned pixels
            queue = [(y, x)]
            while queue:
                y, x = queue.pop()
                if segmented_image[y, x] == 0:
                    segmented_image[y, x] = region_label
                    neighbors = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
                    for y_n, x_n in neighbors:
                        if (0 <= y_n < image.shape[0] and 0 <= x_n < image.shape[1] and
                                segmented_image[y_n, x_n] == 0 and
                                abs(image[y, x] - image[y_n, x_n]) <= threshold):
                            queue.append((y_n, x_n))
            region_label += 1

    return segmented_image

# Load the input image
f = open("MRIBrain.pgm", "r")
p = f.readline()
p1 = f.readline()
p2 = f.readline()
p3 = f.readline()
w, h = [int(i) for i in p2.split()]
image = np.zeros((h, w), np.int64)

for i in range(h):
    for j in range(w):
        image[i, j] = int(f.readline())

f.close()

gray_image = np.zeros_like(image)

# Specify seed points
seed_points = [(50, 100), (50, 100)]  # Example seed points

# Apply region growing
# Perform region growing
segmented_image = region_growing(image, seed_points)

# Save the thresholded image
g = open("regiongrowing.pgm", "w")
g.write("%s" % p)
g.write("%s" % p1)
g.write("%s" % p2)
g.write("%s" % p3)

for i in range(h):
    for j in range(w):
        g.write("%d\n" % segmented_image[i, j])

g.close()
