# LLM Basics — Deeper Notes

*Building on Week 3's intro, based on the "Intro to LLM" video revisit.*

## 1. Quick Recap
- LLMs predict the next token in a sequence, based on everything that came before it.
- They're built on the **Transformer** architecture, which uses **self-attention** to weigh the relevance of every other token when processing a given token.

## 2. Embeddings
- Before a model can do any meaningful computation, tokens need to be converted from discrete symbols (numbers/IDs) into **dense vectors** — this is called an **embedding**.
- These vectors live in a high-dimensional space where semantically similar words end up positioned closer together (e.g., "king" and "queen" would be closer to each other than "king" and "banana").
- Embeddings are *learned* during training — the model figures out on its own what makes words similar or related.

## 3. Context Window
- The context window is the maximum number of tokens a model can process at once (input + output combined).
- Anything beyond that limit gets truncated or dropped, which is why very long documents or conversations can cause a model to "forget" earlier details.
- Larger context windows let models handle longer documents and conversations, but also require more compute.

## 4. Prompting
- **Zero-shot prompting**: asking the model to do a task with no examples, just instructions (e.g., "Summarize this paragraph").
- **Few-shot prompting**: giving the model a few examples of the task before asking it to perform it, which often improves accuracy and consistency.
- Small changes in wording, formatting, or order of instructions can noticeably change the output — this is often called "prompt sensitivity."

## 5. Fine-tuning vs. Prompting
- **Prompting**: the model's weights stay frozen; you guide its behavior purely through the input text. Fast, cheap, no retraining needed.
- **Fine-tuning**: the model's weights are further trained on a specific dataset to specialize its behavior for a task or domain. More effort and compute, but can produce more consistent, specialized results.

## 6. Limitations
- **Hallucinations**: LLMs can generate confident-sounding but factually incorrect information, since they're predicting plausible text, not verifying truth.
- **No true understanding**: the model doesn't "know" facts the way humans do — it's recognizing and reproducing statistical patterns in language.
- **Bias**: since training data comes from real-world text, models can pick up and reproduce biases present in that data.

## Key Takeaway
This week connected the theoretical pieces (tokens, attention) from last week to more practical concepts — embeddings, context windows, and prompting — that directly affect how well an LLM performs on a given task in practice.
