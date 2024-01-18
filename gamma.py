import numpy as np

# Load the image
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

def apply_gamma_transformation(image, gamma):
    transformed_image = np.copy(image)

    # Apply gamma transformation
    transformed_image = np.power(transformed_image, gamma).astype(int)

    return transformed_image

# Set the gamma value
gamma = 0.7  # You can adjust this value based on your requirement

# Apply gamma transformation
img_gamma_transformed = apply_gamma_transformation(img1, gamma)

# Write the result to a new file
with open('images/1_gamma.pgm', 'w') as img_file:
    img_file.write(word)
    img_file.write(comment)
    img_file.write(res)
    img_file.write(str(max_int) + '\n')

    img_gamma_transformed_flat = img_gamma_transformed.reshape(x * y)

    for i in range(x * y):
        img_file.write(str(img_gamma_transformed_flat[i]) + '\n')
