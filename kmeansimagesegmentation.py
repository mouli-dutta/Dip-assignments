import numpy as np

def initialize_centroids(data, k):
    # Randomly initialize centroids
    indices = np.random.choice(len(data), k, replace=False)
    centroids = data[indices]
    return centroids

def assign_to_clusters(data, centroids):
    # Assign each data point to the nearest centroid
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    clusters = np.argmin(distances, axis=1)
    return clusters

def update_centroids(data, clusters, k):
    # Update centroids based on the mean of assigned data points
    centroids = np.array([np.mean(data[clusters == i], axis=0) if np.sum(clusters == i) > 0 else np.mean(data, axis=0) for i in range(k)])
    return centroids

def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)

    for _ in range(max_iterations):
        clusters = assign_to_clusters(data, centroids)
        new_centroids = update_centroids(data, clusters, k)

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, clusters

def rgb_to_flat(data):
    # Flatten RGB image data
    return data.reshape((-1, 3))

def flat_to_rgb(data, shape):
    # Reshape flattened data to the original image shape
    return data.reshape(shape)

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

# Convert RGB image to flat array
data = rgb_to_flat(image)

# Normalize data to the range [0, 1]
data = data / 255.0

# Apply k-means clustering
k = 2  # You can choose the number of clusters
centroids, clusters = kmeans(data, k)

# Assign each pixel the color of its cluster's centroid
segmented_data = centroids[clusters]
segmented_image = flat_to_rgb(segmented_data, image.shape)

# Rescale the segmented image to the original grayscale range
segmented_image = (segmented_image * 255).astype(np.uint8)

# Save the resulting segmented image
with open("segmented_image.pgm", "w") as g:
    g.write("%s" % p)
    g.write("%s" % p1)
    g.write("%s" % p2)
    g.write("%s" % p3)

    for i in range(h):
        for j in range(w):
            g.write("%d\n" % segmented_image[i, j])
