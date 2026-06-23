# LLM Tutorial — Walkthrough Notes

*Notes from the LLM Tutorial video, focused on the practical pipeline.*

## The Text-to-Text Pipeline
A simplified view of how an LLM actually processes a request, end to end:

```
Raw text input
   -> Tokenization        (split text into tokens)
   -> Token IDs            (map each token to a number)
   -> Embeddings            (convert token IDs into dense vectors)
   -> Transformer layers   (self-attention + feed-forward, repeated many times)
   -> Output probabilities (probability distribution over the vocabulary for the next token)
   -> Sampling              (pick the next token, e.g., greedy, top-k, or temperature-based sampling)
   -> Decode back to text
   -> Repeat until a stop condition (e.g., max length or end-of-sequence token)
```

## 1. Tokenization
- Text is split into smaller units (tokens) — these can be whole words, sub-words, or punctuation marks.
- Sub-word tokenization (like Byte Pair Encoding) is common because it handles rare/unseen words better than whole-word tokenization — an unfamiliar word can still be broken into familiar sub-pieces.

## 2. Token IDs & Vocabulary
- Every model has a fixed **vocabulary** — a list of all possible tokens it knows about.
- Each token is mapped to a unique integer ID from this vocabulary.

## 3. Embeddings
- Token IDs are converted into vectors via an embedding layer, giving the model a rich numerical representation to work with instead of just an arbitrary index number.

## 4. Generation Strategies (Sampling)
- **Greedy decoding**: always pick the single most likely next token. Fast, but can produce repetitive or bland text.
- **Top-k sampling**: randomly sample from the top *k* most likely next tokens, adding some variety.
- **Temperature**: controls randomness — lower temperature makes output more focused/predictable, higher temperature makes it more random/creative.

## 5. Why This Matters Practically
- Understanding this pipeline explains *why* certain LLM behaviors happen:
  - Why responses can vary even for the same prompt (sampling randomness)
  - Why very long inputs get cut off (context window limits)
  - Why oddly-spelled or rare words sometimes produce strange outputs (tokenization quirks)

## Key Takeaway
The tutorial made the abstract idea of "an LLM generates text" much more concrete by breaking it into the actual mechanical steps: tokenize → embed → process through Transformer layers → sample the next token → repeat. This pipeline view will be useful when starting to use LLM APIs directly, since parameters like temperature and max tokens map directly to these concepts.
