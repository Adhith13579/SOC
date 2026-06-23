"""
Week 4: N-Gram Language Model + Toy Tokenizer Demo
-----------------------------------------------------
A simple, from-scratch demo to build intuition for "next-token prediction" --
the core idea behind how LLMs generate text, just at a much smaller scale.

Includes:
1. A toy whitespace/punctuation tokenizer
2. A simple n-gram language model that learns next-word probabilities
   from a small training text and can generate new text from them
"""

import random
import re
from collections import defaultdict, Counter


# ----------------------------
# 1. Toy Tokenizer
# ----------------------------
def toy_tokenize(text):
    """
    A very simple tokenizer: lowercases text and splits it into
    words and punctuation marks as separate tokens.
    """
    text = text.lower()
    tokens = re.findall(r"\w+|[^\w\s]", text)
    return tokens


# ----------------------------
# 2. N-Gram Language Model
# ----------------------------
class NGramLanguageModel:
    """
    A simple n-gram model: learns, for every sequence of (n-1) tokens,
    what tokens tend to come next -- and uses that to predict/generate text.
    """

    def __init__(self, n=2):
        self.n = n  # n=2 means bigram (uses 1 previous token to predict the next)
        self.model = defaultdict(Counter)

    def train(self, tokens):
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i + self.n - 1])
            next_token = tokens[i + self.n - 1]
            self.model[context][next_token] += 1

    def predict_next(self, context):
        """Returns the most likely next token(s) given a context, with probabilities."""
        context = tuple(context[-(self.n - 1):])
        if context not in self.model:
            return []
        counts = self.model[context]
        total = sum(counts.values())
        return sorted(
            [(token, round(count / total, 2)) for token, count in counts.items()],
            key=lambda x: -x[1]
        )

    def generate(self, start_context, length=15):
        """Generates new text by repeatedly sampling the next token."""
        context = list(start_context)
        generated = list(start_context)

        for _ in range(length):
            options = self.predict_next(context)
            if not options:
                break
            tokens, weights = zip(*options)
            next_token = random.choices(tokens, weights=weights, k=1)[0]
            generated.append(next_token)
            context.append(next_token)

        return generated


if __name__ == "__main__":
    sample_text = """
    machine learning is a subset of artificial intelligence.
    deep learning is a subset of machine learning.
    machine learning models learn patterns from data.
    deep learning models use neural networks with many layers.
    large language models are a type of deep learning model.
    large language models predict the next token in a sequence.
    """

    print("--- Tokenizing Sample Text ---")
    tokens = toy_tokenize(sample_text)
    print(tokens[:20], "...")
    print(f"Total tokens: {len(tokens)}\n")

    print("--- Training Bigram Language Model ---")
    model = NGramLanguageModel(n=2)
    model.train(tokens)
    print(f"Learned {len(model.model)} unique contexts.\n")

    print("--- Predicting Next Token ---")
    test_context = ["machine"]
    predictions = model.predict_next(test_context)
    print(f"After '{' '.join(test_context)}', possible next tokens: {predictions}\n")

    test_context_2 = ["deep"]
    predictions_2 = model.predict_next(test_context_2)
    print(f"After '{' '.join(test_context_2)}', possible next tokens: {predictions_2}\n")

    print("--- Generating New Text ---")
    random.seed(42)
    generated_tokens = model.generate(["large", "language"], length=12)
    print(" ".join(generated_tokens))
