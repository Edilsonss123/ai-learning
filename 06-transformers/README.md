# Fase 6 — Transformers e LLMs por dentro (meses 8–9)

**Objetivo:** saber exatamente o que acontece entre o texto digitado e o token devolvido, treinar um GPT pequeno e reproduzir resultados de papers.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## Como estudar esta fase

Leitura principal: **Build a Large Language Model (From Scratch)**, de Sebastian Raschka. Acompanhe os capítulos com o código do livro.
Vídeos: Karpathy, *Let's build GPT*, *Let's build the GPT Tokenizer* e *Let's reproduce GPT-2*.
Método: leia o paper da semana **depois** de implementar. O paper fica muito mais claro quando você já escreveu o código.

## Semana a semana

| Semana | Tópicos | Estudar | Praticar |
| --- | --- | --- | --- |
| 1 | Tokenização: caracteres × palavras × subpalavras, BPE, vocabulário, tokens especiais | Raschka, cap. 2; Karpathy, *Let's build the GPT Tokenizer* | [O] BPE treinado em português |
| 2 | Self-attention: query, key, value, produto escalar escalado, softmax | Raschka, cap. 3 (3.1–3.4); Jay Alammar, [*The Illustrated Transformer*](https://jalammar.github.io/illustrated-transformer/); 3Blue1Brown, vídeo sobre atenção | [O] self-attention em NumPy |
| 3 | Máscara causal, multi-head attention, codificação de posição (senoidal, RoPE) | Raschka, cap. 3 (3.5–3.6); paper *Attention Is All You Need*, seções 3.2–3.5 | [O] multi-head com máscara × PyTorch |
| 4 | Bloco Transformer: residual, LayerNorm, MLP; encoder × decoder; BERT × GPT | Raschka, cap. 4; Karpathy, *Let's build GPT*; papers do BERT e do GPT-2 (resumo e arquitetura) | [O] Transformer decoder completo |
| 5 | Pré-treino: próximo token, entropia cruzada, dados, deduplicação, leis de escala | Raschka, cap. 5; papers *Scaling Laws* (Kaplan, 2020) e *Chinchilla* (Hoffmann, 2022), resumo e figuras | [O] nanoGPT em Machado de Assis · experimento de lei de escala |
| 6 | Inferência: logits, temperatura, top-k, top-p, KV cache, janela de contexto | Raschka, cap. 5 (estratégias de decodificação); Karpathy, *Let's reproduce GPT-2* (primeira metade) | [O] comparar amostragens · [C] KV cache · [C] pesos do GPT-2 |
| 7 | Eficiência: mixed precision, quantização, FlashAttention, Mixture of Experts | Karpathy, *Let's reproduce GPT-2* (otimizações); blog de Sebastian Raschka (*Ahead of AI*) sobre MoE e quantização | experimento: LSTM × Transformer · ablação |
| 8 | Interpretabilidade: neurônios, cabeças de atenção, induction heads, circuitos | Artigos da Anthropic sobre interpretabilidade (*Transformer Circuits*), introdução e *induction heads* | reprodução de paper · avaliação · [A] induction heads |

## Sugestões

- Escreva o **shape de cada tensor** em comentário ao lado de cada linha da atenção. 80% dos bugs estão aí.
- Treine o nanoGPT primeiro na sua GPU (modelo de poucos milhões de parâmetros). Para algo próximo do GPT-2, use Colab ou Kaggle.
- A ablação desta fase é o experimento mais revelador da trilha: tire o residual e veja o treino desmoronar.
- [A] Stanford CS336 ([stanford-cs336.github.io](https://stanford-cs336.github.io/)), trabalho 1: o mais profundo disponível.
- [C] Stanford CS224N ([web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/)), aulas de atenção e Transformers.

## Pronto para a avaliação quando

- Explica self-attention com a fórmula e um exemplo numérico de 3 tokens.
- Implementa um Transformer decoder sem `nn.Transformer` e interpreta a própria ablação.
