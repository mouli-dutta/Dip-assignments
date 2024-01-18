import numpy as np

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

def region_split_merge(image, threshold):
    def split_criteria(region):
        # Example criteria: check if the variance is above a threshold
        return np.var(region) > threshold

    def merge_criteria(region1, region2):
        # Example criteria: check if the mean values are close enough
        return abs(np.mean(region1) - np.mean(region2)) < threshold

    stack = [(0, 0, image.shape[1], image.shape[0])]

    while stack:
        start_x, start_y, width, height = stack.pop()

        region = image[start_y:start_y + height, start_x:start_x + width]

        if width == 1 and height == 1:
            continue  # Skip single pixels

        if split_criteria(region):
            half_width = width // 2
            half_height = height // 2

            stack.append((start_x, start_y, half_width, half_height))
            stack.append((start_x + half_width, start_y, half_width, half_height))
            stack.append((start_x, start_y + half_height, half_width, half_height))
            stack.append((start_x + half_width, start_y + half_height, half_width, half_height))
        elif np.isnan(np.sum(region)):
            # Handle NaN values by skipping empty regions
            continue
        else:
            mean_value = np.nanmean(region)  # Use np.nanmean to handle NaN values
            image[start_y:start_y + height, start_x:start_x + width] = mean_value

    return image

threshold_value = 30
img2 = region_split_merge(img1, threshold_value)

with open('images/1_s_m.pgm', 'w') as img:
    img.write(word)
    img.write(comment)
    img.write(res)
    img.write(str(max_int) + '\n')

    img2 = img2.reshape(x * y)

    for i in range(x * y):
        img.write(str(img2[i]) + '\n')