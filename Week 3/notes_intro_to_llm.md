# Intro to Large Language Models (LLMs) — Theory Notes

*Notes based on the "Intro to LLM" and "LLM Tutorial" videos.*

## 1. What is an LLM?
A Large Language Model (LLM) is a deep learning model trained on massive amounts of text data to understand and generate human-like language. Instead of being explicitly programmed with grammar rules, it learns patterns of language — grammar, facts, reasoning patterns, style — directly from the data it's trained on.

## 2. Tokens & Tokenization
- LLMs don't process raw text directly — text is broken down into **tokens** (which can be whole words, sub-words, or even characters depending on the tokenizer).
- Example: the word "unbelievable" might be split into tokens like `un`, `believe`, `able`.
- Each token is mapped to a number, which is what the model actually works with internally.
- The model predicts the **next token** in a sequence, one at a time, based on all the tokens that came before it.

## 3. The Transformer Architecture
- Most modern LLMs (like GPT-style models) are based on the **Transformer** architecture.
- The key innovation is the **self-attention mechanism**, which allows the model to weigh the importance of every other word in a sentence when processing a given word — regardless of how far apart they are.
- This is a major improvement over older architectures (like RNNs), which struggled to capture long-range relationships in text efficiently.
- Transformers can be processed in parallel (rather than strictly sequentially), making them much faster to train on large datasets.

## 4. How LLMs Are Trained
- **Pre-training**: the model is trained on a huge corpus of text (books, websites, articles, etc.) to predict the next token, learning general language patterns and world knowledge.
- **Fine-tuning**: the pre-trained model can then be further trained on more specific data or with human feedback to make it better at particular tasks or more aligned with desired behavior.

## 5. Why LLMs Feel "Intelligent"
- Because they've seen so much text during training, LLMs pick up patterns in reasoning, facts, and language structure that let them generate coherent, context-aware responses.
- They don't "understand" in the human sense — they're predicting the most statistically likely next token based on everything they've learned — but at scale, this produces surprisingly capable and useful behavior.

## 6. Common Applications
- Chatbots and virtual assistants
- Text summarization
- Code generation and debugging help
- Translation
- Content writing and brainstorming

## Key Takeaway
LLMs are a different architecture from CNNs (Transformers + attention vs. convolutions + pooling), but both are built on the same deep learning foundation: layers of learned parameters that transform input data into increasingly useful representations. Understanding tokens, attention, and the two-stage training process (pre-training + fine-tuning) gives a solid conceptual base before diving deeper into how to actually use or build with LLMs.
