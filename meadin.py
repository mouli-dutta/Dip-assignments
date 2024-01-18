import numpy as np

# Load the image
with open('images/3.pgm', 'r') as img:
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
    
def apply_median_filter(image):

    filtered_image = np.copy(image)

    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # Get the 3x3 neighborhood
            neighborhood = [image[i - 1, j - 1], image[i, j - 1], image[i + 1, j - 1],
                            image[i - 1, j], image[i, j], image[i + 1, j],
                            image[i - 1, j + 1], image[i, j + 1], image[i + 1, j + 1]]

            # Apply median filter
            filtered_image[i, j] = np.median(neighborhood)

    return filtered_image

# Apply median filter
img_median_filtered = apply_median_filter(img1)

# Write the result to a new file
with open('images/3_median.pgm', 'w') as img_file:
    img_file.write(word)
    img_file.write(comment)
    img_file.write(res)
    img_file.write(str(max_int) + '\n')

    img_median_filtered_flat = img_median_filtered.reshape(x * y)

    for i in range(x * y):
        img_file.write(str(img_median_filtered_flat[i]) + '\n')
