# Week 3: Deep Learning & CNN 

##  Goals
- [x] Understand the basics of Deep Learning
- [x] Learn how Convolutional Neural Networks (CNNs) work
- [x] Get an intro to Large Language Models (LLMs)

## Resources Used
- **Intro to LLM** video — high-level overview of what LLMs are and how they work
- **LLM Tutorial** video — deeper dive into LLM concepts (tokens, transformers, training)

##  What I Covered

### Deep Learning Basics
- What a neural network is: neurons, weights, biases, layers
- Activation functions (ReLU, Sigmoid, Softmax) and why non-linearity matters
- Forward propagation and a conceptual understanding of backpropagation
- Loss functions and gradient descent as the "learning" mechanism

### Convolutional Neural Networks (CNNs)
- Why CNNs are used for image data instead of plain neural networks
- Core building blocks: **convolution layers**, **filters/kernels**, **feature maps**
- **Pooling layers** (max pooling) for downsampling and reducing computation
- Typical CNN architecture: `Input -> Conv -> Pool -> Conv -> Pool -> Flatten -> Fully Connected -> Output`
- Common use cases: image classification, object detection

Detailed notes: [`notes_deep_learning_cnn.md`](./notes_deep_learning_cnn.md)

### Intro to LLMs (Large Language Models)
- What an LLM is and how it's trained on large amounts of text data
- Tokens and tokenization — how text gets converted into a format models understand
- The **Transformer** architecture and the role of **self-attention**
- Why LLMs can generate coherent, context-aware text
- Examples of LLMs (GPT-style models) and their common applications

Detailed notes: [`notes_intro_to_llm.md`](./notes_intro_to_llm.md)

### Hands-on
- Implemented convolution and max pooling **from scratch using NumPy** to understand what's actually happening "under the hood" in a CNN, before relying on frameworks like PyTorch/TensorFlow.

Code: [`cnn_concepts_demo.py`](./cnn_concepts_demo.py)

##  Notes to Self
- CNNs make a lot more sense now that I understand why convolution + pooling is better than feeding raw pixels into a normal neural network (fewer parameters, captures spatial patterns).
- LLMs are a different beast from CNNs — attention mechanisms instead of convolutions — but the core idea of "layers learning representations" still connects back to the neural network basics.
- Next week: start implementing a real CNN using a framework (PyTorch/TensorFlow) on an actual image dataset.
