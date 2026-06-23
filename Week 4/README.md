# Week 4: Intro to LLM 

##  Goals
- [x] Build on last week's LLM intro with a deeper, more practical understanding
- [x] Go through the LLM Tutorial video and connect concepts to actual implementation ideas

##  Resources Used
- **Intro to LLM** video — revisited for a refresher on core concepts
- **LLM Tutorial** video — focused on tokenization, embeddings, and how prompting/fine-tuning actually work in practice

##  What I Covered

### LLM Basics (Going Deeper)
- Quick recap: tokens, the Transformer architecture, self-attention
- **Embeddings** — how tokens get converted into dense numerical vectors that capture semantic meaning (similar words end up closer together in vector space)
- **Context window** — the limited amount of text (tokens) a model can "see" at once, and why this matters for long conversations/documents
- **Prompting** — how the way you phrase an input affects the output (zero-shot vs few-shot prompting)
- **Fine-tuning vs. Prompting** — adapting a model's weights vs. just guiding a frozen model with good instructions
- Limitations: hallucinations, lack of true "understanding," sensitivity to prompt phrasing

Detailed notes: [`notes_llm_basics.md`](./notes_llm_basics.md)

### LLM Tutorial Walkthrough
- Notes from the tutorial video, focused on the practical side: how text actually flows through tokenization → embeddings → model → output tokens → decoded text

Detailed notes: [`llm_tutorial_notes.md`](./llm_tutorial_notes.md)

### Hands-on
- Built a simple **n-gram language model from scratch** to get an intuitive feel for "next-token prediction" — the core idea behind how LLMs generate text, just at a much smaller and simpler scale.
- Also wrote a basic **toy tokenizer** to see how raw text gets split into tokens before being fed to a model.

Code: [`ngram_language_model_demo.py`](./ngram_language_model_demo.py)

##  Notes to Self
- It really clicked this week that an LLM is, at its core, just a (very sophisticated) next-token predictor — the n-gram demo made that concept tangible even without all the Transformer complexity.
- Prompting matters a lot more than I expected — same question phrased differently can give noticeably different results.
- Next step: explore using an actual LLM API to apply prompting techniques on real tasks (summarization, Q&A, etc.).
