"""
Week 3: CNN Concepts Demo (from scratch using NumPy)
------------------------------------------------------
Before using a framework like PyTorch/TensorFlow, this script implements
the core CNN operations manually to understand what's happening under
the hood: convolution and max pooling.
"""

import numpy as np


def convolve2d(image, kernel, stride=1):
    """
    Applies a 2D convolution (valid padding) of `kernel` over `image`.
    Returns the resulting feature map.
    """
    img_h, img_w = image.shape
    k_h, k_w = kernel.shape

    out_h = (img_h - k_h) // stride + 1
    out_w = (img_w - k_w) // stride + 1

    feature_map = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            row_start = i * stride
            col_start = j * stride
            patch = image[row_start:row_start + k_h, col_start:col_start + k_w]
            feature_map[i, j] = np.sum(patch * kernel)

    return feature_map


def max_pool2d(feature_map, pool_size=2, stride=2):
    """
    Applies max pooling over `feature_map`.
    """
    f_h, f_w = feature_map.shape
    out_h = (f_h - pool_size) // stride + 1
    out_w = (f_w - pool_size) // stride + 1

    pooled = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            row_start = i * stride
            col_start = j * stride
            patch = feature_map[row_start:row_start + pool_size, col_start:col_start + pool_size]
            pooled[i, j] = np.max(patch)

    return pooled


def relu(x):
    """Applies the ReLU activation function element-wise."""
    return np.maximum(0, x)


if __name__ == "__main__":
    # A simple 6x6 "image" (think of it as grayscale pixel values)
    image = np.array([
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1],
    ])

    # A simple vertical edge detector filter
    edge_filter = np.array([
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1],
    ])

    print("--- Original Image ---")
    print(image)

    feature_map = convolve2d(image, edge_filter)
    print("\n--- Feature Map after Convolution (edge detection) ---")
    print(feature_map)

    activated = relu(feature_map)
    print("\n--- After ReLU Activation ---")
    print(activated)

    pooled = max_pool2d(activated, pool_size=2, stride=2)
    print("\n--- After Max Pooling (2x2) ---")
    print(pooled)

    print("\nOriginal shape:", image.shape)
    print("Feature map shape after convolution:", feature_map.shape)
    print("Shape after max pooling:", pooled.shape)
