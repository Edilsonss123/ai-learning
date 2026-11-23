# Referências — Fase 6: Transformers e LLMs por dentro

## O que você vai aprender

- **Tokenização**: como o texto vira números (BPE) e por que isso explica erros curiosos dos LLMs.
- **Self-attention**: query, key, value, produto escalar escalado e softmax, com a matemática e o código.
- Multi-head attention, máscara causal e codificação de posição (senoidal e RoPE).
- O **bloco Transformer** completo (residual, LayerNorm, MLP) e a diferença entre encoder (BERT) e decoder (GPT).
- **Pré-treino**: previsão do próximo token, dados, deduplicação e **leis de escala** (Kaplan, Chinchilla).
- **Inferência**: logits, temperatura, top-k, top-p, KV cache e janela de contexto.
- Eficiência (mixed precision, quantização, FlashAttention, Mixture of Experts) e noções de **interpretabilidade**.
- Ler, implementar e reproduzir resultados de papers.

## Material principal

| Material | Tipo | Onde usar |
| --- | --- | --- |
| *Build a Large Language Model (From Scratch)* — Sebastian Raschka | livro | caps. 2–5 |
| Karpathy: *Let's build GPT*, *Let's build the GPT Tokenizer*, *Let's reproduce GPT-2* | vídeo | semanas 1, 4, 6, 7 |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar | artigo | semana 2 |
| [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017) | paper | semanas 3–4 |
| [nanoGPT](https://github.com/karpathy/nanoGPT) — Karpathy | código | semana 5 |

## Materiais alternativos

**Implementações comentadas**
- [*The Annotated Transformer*](https://nlp.seas.harvard.edu/annotated-transformer/) — Harvard NLP: o paper original linha a linha, em PyTorch.
- [llm.c](https://github.com/karpathy/llm.c) — Karpathy: GPT-2 em C/CUDA puro, para entender o que o PyTorch faz por baixo. [A]

**Livros**
- *Natural Language Processing with Transformers* — Tunstall, von Werra, Wolf (Hugging Face): prático, com a biblioteca Transformers.
- *Hands-On Large Language Models* — Jay Alammar e Maarten Grootendorst: muito visual. [C]

**Cursos**
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/): o mais profundo disponível. [A]
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/): aulas de atenção, Transformers e pré-treino. [C]
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course), caps. 1–4: o lado prático com a biblioteca.

**Vídeos e blogs**
- 3Blue1Brown, capítulos da série *Neural Networks* sobre Transformers e atenção.
- Andrej Karpathy, *Intro to Large Language Models* (palestra de 1 hora): visão geral.
- Blog de Lilian Weng (lilianweng.github.io): revisões profundas sobre atenção e Transformers.
- Blog de Sebastian Raschka, *Ahead of AI*: novidades de arquitetura explicadas.
- [Transformer Circuits](https://transformer-circuits.pub/) (Anthropic): interpretabilidade. [A]
