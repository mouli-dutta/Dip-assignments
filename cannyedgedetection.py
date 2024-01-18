import numpy as np


def gaussian_blur(image, sigma=1.0):
    # Create a 1D Gaussian kernel
    kernel_size = int(6 * sigma)
    if kernel_size % 2 == 0:
        kernel_size += 1

    kernel = np.fromfunction(
        lambda x: (1/ (2 * np.pi * sigma ** 2)) * np.exp(-((x - (kernel_size - 1) / 2) ** 2) / (2 * sigma ** 2)),
        (kernel_size,)
    )

    # Normalize the kernel
    kernel /= np.sum(kernel)

    # Apply convolution along rows
    blurred_image = np.apply_along_axis(lambda row: np.convolve(row, kernel, mode='same'), axis=1, arr=image)

    # Transpose and apply convolution along columns
    blurred_image = np.apply_along_axis(lambda col: np.convolve(col, kernel, mode='same'), axis=0, arr=blurred_image)

    return blurred_image

def sobel_operator(blurred_image):
    # Apply the Sobel operator to detect edges
    height, width = blurred_image.shape
    gradient_magnitude = np.zeros((height, width))
    gradient_direction = np.zeros((height, width))

    for i in range(1, height-1):
        for j in range(1, width-1):
            gx = (blurred_image[i+1, j-1] + 2 * blurred_image[i+1, j] + blurred_image[i+1, j+1]) - \
                 (blurred_image[i-1, j-1] + 2 * blurred_image[i-1, j] + blurred_image[i-1, j+1])

            gy = (blurred_image[i-1, j+1] + 2 * blurred_image[i, j+1] + blurred_image[i+1, j+1]) - \
                 (blurred_image[i-1, j-1] + 2 * blurred_image[i, j-1] + blurred_image[i+1, j-1])
                 
            gradient_magnitude[i, j] = np.sqrt(gx**2 + gy**2)
            gradient_direction[i, j] = np.arctan2(gy, gx)

            

    return gradient_magnitude, gradient_direction

def non_max_suppression(gradient_magnitude, gradient_direction):
    # Perform non-maximum suppression
    height, width = gradient_magnitude.shape
    suppressed_image = np.zeros_like(gradient_magnitude)

    for i in range(1, height-1):
        for j in range(1, width-1):
            angle = gradient_direction[i, j]

            if 0 <= angle < np.pi / 4 or 7 * np.pi / 4 <= angle:
                neighbors = [gradient_magnitude[i, j-1], gradient_magnitude[i+1, j-1], gradient_magnitude[i+1, j]]
            elif np.pi / 4 <= angle < 2 * np.pi / 4 or 5 * np.pi / 4 <= angle < 7 * np.pi / 4:
                neighbors = [gradient_magnitude[i+1, j-1], gradient_magnitude[i+1, j], gradient_magnitude[i+1, j+1]]
            elif 2 * np.pi / 4 <= angle < 3 * np.pi / 4 or 3 * np.pi / 4 <= angle < 5 * np.pi / 4:
                neighbors = [gradient_magnitude[i, j-1], gradient_magnitude[i+1, j], gradient_magnitude[i, j+1]]
            else:
                neighbors = [gradient_magnitude[i-1, j+1], gradient_magnitude[i-1, j], gradient_magnitude[i-1, j-1]]

            if gradient_magnitude[i, j] >= max(neighbors):
                suppressed_image[i, j] = gradient_magnitude[i, j]

    return suppressed_image

def edge_tracking_by_hysteresis(suppressed_image, low_threshold, high_threshold):
    # Perform edge tracking by hysteresis
    height, width = suppressed_image.shape
    result_image = np.zeros_like(suppressed_image)

    strong_edges = suppressed_image > high_threshold
    weak_edges = (suppressed_image >= low_threshold) & (suppressed_image <= high_threshold)

    result_image[strong_edges] = 255
    visited = set()

    for i in range(1, height-1):
        for j in range(1, width-1):
            if (i, j) in visited or not weak_edges[i, j]:
                continue

            edge_pixels = set()
            stack = [(i, j)]

            while stack:
                current_pixel = stack.pop()
                edge_pixels.add(current_pixel)
                visited.add(current_pixel)

                neighbors = [
                    (current_pixel[0] + 1, current_pixel[1]),
                    (current_pixel[0] - 1, current_pixel[1]),
                    (current_pixel[0], current_pixel[1] + 1),
                    (current_pixel[0], current_pixel[1] - 1),
                    (current_pixel[0] + 1, current_pixel[1] + 1),
                    (current_pixel[0] - 1, current_pixel[1] - 1),
                    (current_pixel[0] + 1, current_pixel[1] - 1),
                    (current_pixel[0] - 1, current_pixel[1] + 1),
                ]

                for neighbor in neighbors:
                    if 0 <= neighbor[0] < height and 0 <= neighbor[1] < width and neighbor not in visited and weak_edges[neighbor]:
                        stack.append(neighbor)

            if len(edge_pixels) > 0:
                for pixel in edge_pixels:
                    result_image[pixel] = 255

    return result_image
    
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



# Apply Gaussian blur
blurred_image = gaussian_blur(image, sigma=1.0)

print("Shape of blurred_image:", blurred_image.shape)

# Apply Sobel operator
gradient_magnitude, gradient_direction = sobel_operator(blurred_image)

# Print the shape of gradient_magnitude
print("Shape of gradient_magnitude:", gradient_magnitude.shape)

# Non-maximum suppression
suppressed_image = non_max_suppression(gradient_magnitude, gradient_direction)

# Edge tracking by hysteresis
low_threshold = 20  # Adjust as needed
high_threshold = 50  # Adjust as needed
result_image = edge_tracking_by_hysteresis(suppressed_image, low_threshold, high_threshold)

# Save the resulting edges image
with open("CANNY_edge_detect.pgm", "w") as g:
    g.write("%s" % p)
    g.write("%s" % p1)
    g.write("%s" % p2)
    g.write("%s" % p3)

    for i in range(h):
        for j in range(w):
            g.write("%d\n" % suppressed_image[i, j])
            
            
# Save the resulting edges image
with open("CANNY_edge_detect1.pgm", "w") as g:
    g.write("%s" % p)
    g.write("%s" % p1)
    g.write("%s" % p2)
    g.write("%s" % p3)

    for i in range(h):
        for j in range(w):
            g.write("%d\n" % result_image[i, j])
            
