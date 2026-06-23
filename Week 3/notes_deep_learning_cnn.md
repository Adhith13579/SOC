# Deep Learning & CNN — Theory Notes

## 1. Deep Learning Basics

### What is a Neural Network?
A neural network is made up of layers of connected "neurons":
- **Input layer** — receives the raw data (e.g., pixel values)
- **Hidden layer(s)** — learn intermediate representations/patterns
- **Output layer** — produces the final prediction

Each connection has a **weight**, and each neuron has a **bias**. A neuron computes a weighted sum of its inputs, adds the bias, and passes the result through an **activation function**.

### Activation Functions
Activation functions introduce non-linearity, allowing the network to learn complex patterns instead of just straight lines:
- **ReLU (Rectified Linear Unit)** — outputs 0 for negative inputs, and the input itself for positive ones. Most common in hidden layers.
- **Sigmoid** — squashes output between 0 and 1, often used for binary classification outputs.
- **Softmax** — converts a vector of numbers into probabilities that sum to 1, used for multi-class classification outputs.

### Forward Propagation & Backpropagation
- **Forward propagation**: data flows from the input layer through hidden layers to the output, producing a prediction.
- **Loss function**: measures how far the prediction is from the actual answer (e.g., Mean Squared Error for regression, Cross-Entropy for classification).
- **Backpropagation**: the error is propagated backward through the network to compute how much each weight contributed to the error.
- **Gradient Descent**: weights are updated step-by-step in the direction that reduces the loss, using a **learning rate** to control step size.

## 2. Convolutional Neural Networks (CNNs)

### Why not just use a regular neural network for images?
- Images have a huge number of pixels — feeding every pixel into a fully connected layer creates an enormous number of parameters.
- Regular neural networks don't account for **spatial structure** (nearby pixels are related).
- CNNs solve this by using small filters that scan across the image, reusing the same parameters everywhere — far more efficient and better at capturing local patterns like edges and textures.

### Core Building Blocks

**Convolution Layer**
- A small matrix called a **filter/kernel** (e.g., 3x3) slides over the image.
- At each position, it computes a dot product between the filter and the patch of the image it's covering, producing a single value.
- Doing this across the whole image produces a **feature map** — a transformed version of the image highlighting certain patterns (edges, corners, etc.).
- Multiple filters are used in a layer, each learning to detect different features.

**Pooling Layer**
- Used to reduce the size of feature maps (downsampling), which reduces computation and helps prevent overfitting.
- **Max Pooling** is the most common type — it takes the maximum value from each small region (e.g., 2x2) of the feature map.

**Flatten + Fully Connected Layer**
- After several convolution + pooling layers, the resulting feature maps are flattened into a single vector.
- This vector is passed into one or more fully connected layers, which combine the extracted features to make the final prediction.

### Typical CNN Architecture
```
Input Image
   -> Convolution Layer -> Activation (ReLU)
   -> Pooling Layer
   -> Convolution Layer -> Activation (ReLU)
   -> Pooling Layer
   -> Flatten
   -> Fully Connected Layer
   -> Output Layer (Softmax for classification)
```

### Common Use Cases
- Image classification (e.g., cat vs. dog)
- Object detection
- Facial recognition
- Medical image analysis

## Key Takeaway
Deep Learning extends basic neural networks with more layers and specialized architectures. CNNs are specifically designed to handle image data efficiently by exploiting spatial structure through convolution and pooling, instead of treating every pixel independently like a plain neural network would.
