# Plano de estudos: de usuário a especialista em IA

12 meses, 8 fases, 8 a 10 horas por semana. A ordem segue uma formação progressiva: **história → teoria → matemática → implementação → experimentação → aplicação real**. Você só avança de fase depois de passar na avaliação do mês.

Este arquivo traz o **conteúdo** de cada fase (semanas, leituras, cursos, papers). Os **exercícios, experimentos e a avaliação** de cada fase ficam no `PROGRESSO.md` da pasta, que é de onde o painel lê o progresso. As regras de organização estão no [`CLAUDE.md`](CLAUDE.md).

| Etapa da formação | Fases | Meses |
| --- | --- | --- |
| História | 1. História da IA e fracassos | 1 |
| Teoria | 2. IA clássica: lógica, busca, sistemas especialistas, RL | 2 |
| Matemática | 3. Matemática para IA | 3–4 |
| Implementação | 4. ML clássico · 5. Redes neurais e deep learning | 5–7 |
| Experimentação | 6. Transformers e LLMs | 8–9 |
| Aplicação real | 7. Pós-treino, RAG, agentes, produção · 8. Projeto final | 10–12 |

## Regras gerais

### Níveis de exercício

| Nível | Significado | Tempo típico |
| --- | --- | --- |
| **[O] Obrigatório** | condição para passar na avaliação | cabe em 8 h/semana com a teoria |
| **[C] Complementar** | aprofunda; faça se sobrar tempo | +1 a 2 h/semana (até 10 h) |
| **[A] Avançado** | desafio opcional; volte depois da trilha | fora do orçamento |

Semana típica de 8 h: 2,5 h de teoria (livro e aula), 4 h de implementação, 1,5 h de experimento e registro.

### Avaliação mensal: três capacidades para avançar

1. **Explicar**: explicar o conceito sem consultar notas, como se fosse para um colega júnior.
2. **Implementar**: implementar sem bibliotecas de alto nível (só Python e NumPy, ou PyTorch básico a partir da Fase 5).
3. **Analisar**: rodar, medir e explicar o resultado: o que funcionou, onde falhou e por quê.

Passe nas três, ou repita as semanas fracas antes de seguir. Evidências em `AVALIACAO.md` (modelo em [`templates/`](templates/)).

### Método experimental

Todo experimento segue o roteiro de [`templates/EXPERIMENTO.md`](templates/EXPERIMENTO.md): pergunta → hipótese → setup (semente fixa) → resultado → análise de erros (20 erros, um por um) → ablação (tirar uma peça por vez) → conclusão (por que funcionou ou fracassou).

### Setup

- Python: comece na Fase 1, semana 1, em paralelo com a história. Vindo de C#, o [tutorial oficial](https://docs.python.org/3/tutorial/) e NumPy bastam.
- Ambiente: WSL2 (Ubuntu), VS Code + Jupyter, `uv`, PyTorch com CUDA. GPU gratuita no [Google Colab](https://colab.research.google.com/) ou no Kaggle.

---

## Fase 1 — História da IA, primeiros modelos e fracassos (mês 1)

Objetivo: entender de onde vêm as ideias atuais, por que a IA passou por dois "invernos" e o que cada fracasso ensinou.

| Semana | Tema | Paralelo |
| --- | --- | --- |
| 1 | Origens: McCulloch & Pitts (1943), Turing (1950), Dartmouth (1956) | Python básico |
| 2 | Primeiros modelos: perceptron (1958), ELIZA (1966), IA simbólica | NumPy |
| 3 | Fracassos e invernos: ALPAC, *Perceptrons* e XOR, Lighthill, Quinta Geração, Lisp machines | — |
| 4 | A retomada: backprop (1986), LeNet, AlexNet (2012), Transformer (2017), GPT-3, ChatGPT; fracassos recentes | avaliação |

**Linha do tempo de referência**

| Ano | Marco | Lição |
| --- | --- | --- |
| 1943 | Neurônio de McCulloch & Pitts | primeiro modelo matemático de neurônio |
| 1950 | Turing, *Computing Machinery and Intelligence* | a pergunta "máquinas podem pensar?" |
| 1956 | Conferência de Dartmouth | nasce o termo "IA"; previsões otimistas demais |
| 1958 | Perceptron de Rosenblatt | primeira máquina que aprende com dados |
| 1966 | ELIZA; relatório ALPAC | **fracasso**: tradução automática não entregou e perdeu verba |
| 1969 | *Perceptrons*, Minsky & Papert | **fracasso**: perceptron de 1 camada não resolve XOR |
| 1973 | Relatório Lighthill | **primeiro inverno da IA** |
| anos 80 | Sistemas especialistas (MYCIN, XCON) | funcionam em nicho, mas manter regras à mão não escala |
| 1982–92 | Quinta Geração (Japão) | **fracasso**: hardware lógico massivo não virou inteligência |
| 1984–hoje | Projeto Cyc | **fracasso parcial**: senso comum codificado à mão nunca terminou |
| 1986 | Backpropagation | redes multicamada voltam a ser treináveis |
| 1987 | Colapso das Lisp machines | **segundo inverno da IA** |
| 1997 | Deep Blue; LSTM | busca força bruta vence xadrez; memória em redes |
| 2012 | AlexNet | GPU + dados = deep learning moderno |
| 2016 | AlphaGo; Tay (Microsoft) | RL + redes vence Go; **fracasso**: Tay ficou ofensivo em 16 h |
| 2017 | *Attention Is All You Need* | o Transformer |
| 2022 | ChatGPT; Galactica (Meta) | RLHF torna LLMs úteis; **fracasso**: Galactica retirado em 3 dias |

Também vale estudar **Google Flu Trends** (overfitting a buscas) e **IBM Watson Health** (promessa em oncologia não sustentada).

**Leitura**
- *Inteligência Artificial: Uma Abordagem Moderna* — Russell & Norvig, cap. 1 ([site](https://aima.cs.berkeley.edu/)).
- *Artificial Intelligence: A Guide for Thinking Humans* — Melanie Mitchell.
- *Genius Makers* — Cade Metz. [C]
- *The Quest for Artificial Intelligence* — Nils Nilsson. [A]

Exercícios, experimento e avaliação: [`01-historia/PROGRESSO.md`](01-historia/PROGRESSO.md).

## Fase 2 — IA clássica: lógica, busca, sistemas especialistas e RL (mês 2)

Objetivo: conhecer as abordagens anteriores ao deep learning que ainda vivem em sistemas modernos: a busca no AlphaGo, a lógica em verificadores, o RL no RLHF dos LLMs.

| Semana | Tema |
| --- | --- |
| 1 | Busca: espaço de estados, BFS, DFS, custo uniforme, A* e heurísticas admissíveis |
| 2 | Jogos e restrições: minimax, poda alfa-beta, CSP |
| 3 | Lógica e conhecimento: proposicional e de primeira ordem, inferência, sistemas especialistas (encadeamento para frente e para trás) |
| 4 | Aprendizado por reforço: agente, ambiente, recompensa, MDP, exploração × aproveitamento (bandits), Q-learning tabular |

**Leitura e cursos**
- Russell & Norvig, caps. 3–6 (busca, jogos, CSP) e 7–9 (lógica).
- [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) — Sutton & Barto (gratuito), caps. 1–3 e 6.
- [CS50's Introduction to AI with Python](https://cs50.harvard.edu/ai/) — Search, Knowledge, Optimization. Curso principal da fase.
- [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course) — unidades 1–2. [C]

Exercícios, experimento e avaliação: [`02-ia-classica/PROGRESSO.md`](02-ia-classica/PROGRESSO.md).

## Fase 3 — Matemática para IA (meses 3–4)

Objetivo: ler qualquer fórmula de rede neural e implementá-la em NumPy. São 8 semanas.

| Semana | Tema | O que precisa sair sabendo |
| --- | --- | --- |
| 1 | Vetores | soma, escala, produto escalar, norma, similaridade de cosseno |
| 2 | Matrizes | multiplicação, transposta, inversa, matriz como transformação |
| 3 | Decomposições | autovalores, autovetores, SVD (intuição), tensores |
| 4 | Cálculo | derivada, derivada parcial, gradiente |
| 5 | Regra da cadeia | derivadas compostas, jacobiano, grafo computacional |
| 6 | Probabilidade | condicional, Bayes, distribuições, esperança, variância |
| 7 | Estatística e informação | máxima verossimilhança, entropia, entropia cruzada, KL |
| 8 | Otimização | função de perda, gradiente descendente, taxa de aprendizado, SGD |

A regra central da trilha: **w ← w − η · ∂L/∂w**, em que η é a taxa de aprendizado e L a função de perda.

**Leitura e cursos**
- [Mathematics for Machine Learning](https://mml-book.github.io/) — Deisenroth, Faisal, Ong (gratuito), caps. 2, 4, 5, 6, 7.
- [3Blue1Brown](https://www.3blue1brown.com/): *Essence of Linear Algebra* e *Essence of Calculus*.
- [Khan Academy](https://pt.khanacademy.org/) em português, para tapar buracos.
- *Mathematics for Machine Learning and Data Science* — DeepLearning.AI (Coursera). [C]

Exercícios, experimento e avaliação: [`03-matematica/PROGRESSO.md`](03-matematica/PROGRESSO.md).

## Fase 4 — Machine learning clássico (mês 5)

Objetivo: dominar o ciclo dados → modelo → avaliação → análise de erros.

| Semana | Tema |
| --- | --- |
| 1 | Supervisionado × não supervisionado; regressão logística; treino/validação/teste |
| 2 | Overfitting, viés × variância, regularização L1/L2, validação cruzada, vazamento de dados |
| 3 | k-NN, árvores, random forest, gradient boosting (XGBoost/LightGBM), SVM |
| 4 | Métricas (precisão, recall, F1, ROC-AUC, calibração), k-means, PCA, pipelines no scikit-learn |

**Leitura e cursos**
- [An Introduction to Statistical Learning (ISLP)](https://www.statlearning.com/) — gratuito, em Python, caps. 2–5 e 8.
- *Hands-On Machine Learning* — Aurélien Géron, parte I. [C]
- *Machine Learning Specialization* — Andrew Ng (Coursera), cursos 1 e 2.
- [Kaggle Learn](https://www.kaggle.com/learn) — Intro e Intermediate ML.

Exercícios, experimentos e avaliação: [`04-ml-classico/PROGRESSO.md`](04-ml-classico/PROGRESSO.md).

## Fase 5 — Redes neurais e deep learning (meses 6–7)

Objetivo: escrever o backpropagation à mão antes de usar PyTorch. 8 semanas; as 4 primeiras só para redes e backprop.

| Semana | Tema |
| --- | --- |
| 1 | Neurônio, pesos, bias, ativações, forward pass, perdas |
| 2 | Backpropagation, grafo computacional, autograd (micrograd) |
| 3 | SGD, momentum, Adam, inicialização, gradientes que somem ou explodem |
| 4 | PyTorch: tensores, `nn.Module`, `DataLoader`, loop de treino, GPU |
| 5 | BatchNorm/LayerNorm, dropout, learning rate schedule, diagnóstico de curvas |
| 6 | CNNs: convolução, pooling, LeNet → AlexNet → ResNet |
| 7 | RNN, LSTM, GRU; por que perderam para o Transformer |
| 8 | Embeddings (word2vec), Seq2Seq e a primeira atenção (Bahdanau) |

**Leitura e cursos**
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — Andrej Karpathy, vídeos 1–5. **Curso principal da trilha.**
- [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) — gratuito, com código PyTorch.
- [Deep Learning](https://www.deeplearningbook.org/) — Goodfellow, Bengio, Courville. [C]
- *Understanding Deep Learning* — Simon Prince (gratuito). [C]
- [Practical Deep Learning for Coders](https://course.fast.ai/) — fast.ai. [C]

**Papers**: Rumelhart, Hinton, Williams (1986), backprop · Krizhevsky et al. (2012), AlexNet · He et al. (2015), ResNet.

Exercícios, experimentos e avaliação: [`05-deep-learning/PROGRESSO.md`](05-deep-learning/PROGRESSO.md).

## Fase 6 — Transformers e LLMs por dentro (meses 8–9)

Objetivo: saber o que acontece entre o texto digitado e o token devolvido, treinar um GPT pequeno e reproduzir resultados de papers.

| Semana | Tema |
| --- | --- |
| 1 | Tokenização: BPE, vocabulário |
| 2 | Self-attention: query, key, value, produto escalar escalado, softmax |
| 3 | Multi-head, máscara causal, posição (senoidal e RoPE) |
| 4 | Bloco Transformer: residual, LayerNorm, MLP; BERT × GPT |
| 5 | Pré-treino: próximo token, dados, deduplicação, leis de escala (Kaplan, Chinchilla) |
| 6 | Inferência: logits, temperatura, top-k, top-p, KV cache, contexto |
| 7 | Eficiência: mixed precision, quantização, FlashAttention, Mixture of Experts |
| 8 | Interpretabilidade: neurônios, cabeças de atenção, circuitos |

**Leitura e cursos**
- *Build a Large Language Model (From Scratch)* — Sebastian Raschka. Leitura principal.
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar.
- Karpathy: *Let's build GPT*, *Let's build the GPT Tokenizer*, *Let's reproduce GPT-2*.
- [Stanford CS336](https://stanford-cs336.github.io/): trabalho 1. [A]
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/): aulas de atenção e Transformers. [C]

**Papers**: [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762) (2017) · BERT (2018) · GPT-2 (2019) · Scaling Laws (2020) · Chinchilla (2022).

Exercícios, experimentos e avaliação: [`06-transformers/PROGRESSO.md`](06-transformers/PROGRESSO.md).

## Fase 7 — Pós-treino, RAG, agentes e produção (meses 10–11)

Objetivo: transformar um modelo base em assistente e construir sistemas confiáveis sobre LLMs. O RL da Fase 2 volta como RLHF.

| Semana | Tema |
| --- | --- |
| 1 | SFT com instruções; por que o modelo base não "conversa" |
| 2 | RLHF (PPO), DPO, Constitutional AI |
| 3 | LoRA, QLoRA, PEFT; ajustar × só prompt |
| 4 | Prompting: few-shot, chain-of-thought, saídas estruturadas |
| 5 | RAG: chunking, embeddings, pgvector/Qdrant, busca híbrida, reranking |
| 6 | Agentes: tool calling, MCP, planejamento, memória |
| 7 | Evals: conjuntos de teste, LLM-como-juiz, regressão de qualidade |
| 8 | Produção: latência, custo por token, cache, observabilidade, Ollama, vLLM |
| 9 | Segurança: alucinação, prompt injection, vazamento, LGPD, permissões, auditoria |

**Leitura e cursos**
- *AI Engineering* — Chip Huyen. Leitura principal.
- *Hands-On Large Language Models* — Alammar e Grootendorst. [C]
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) e [Agents Course](https://huggingface.co/learn/agents-course).
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/) (RAG, agentes, evals).
- [Anthropic Courses](https://github.com/anthropics/courses). [C]

**Papers**: LoRA (2021) · InstructGPT (2022) · DPO (2023) · RAG (Lewis et al., 2020) · ReAct (2022).

Exercícios, experimentos e avaliação: [`07-aplicacao/PROGRESSO.md`](07-aplicacao/PROGRESSO.md).

## Fase 8 — Projeto final e reprodução de paper (mês 12)

Objetivo: juntar as Fases 2 a 7 num **assistente de negociação de dívidas** que entende a pergunta do devedor, busca regras e ofertas via RAG, estima a chance de aceite com um modelo clássico e chama APIs de simulação por tool calling. Só dados fictícios.

| Semana | Entrega |
| --- | --- |
| 1 | Problema, requisitos, métricas, dataset sintético e baseline de regras (Fase 2) |
| 2 | Backend .NET, RAG, classificador de aceite, agente |
| 3 | Avaliação, testes de segurança e desempenho; comparação com o baseline |
| 4 | Documentação, publicação e post técnico |

Em paralelo (2 h/semana): reproduzir um resultado de paper usando [`templates/PAPER.md`](templates/PAPER.md).

Exercícios e avaliação final: [`08-projeto-final/PROGRESSO.md`](08-projeto-final/PROGRESSO.md).

**Depois dos 12 meses**: *AI engineering* é o caminho mais natural; as alternativas são *ML research*, *MLOps* e *segurança e interpretabilidade*. Mantenha 1 paper por semana e 1 reprodução por trimestre.

---

## Hardware

Máquina atual: i5-9300H, 24 GB de RAM, GPU de 4 GB. Roda cerca de 80% da trilha.

| Fases | Local? | Alternativa |
| --- | --- | --- |
| 1–4 | Sim, só CPU | — |
| 5 (MLP, CNN, makemore) | Sim, na GPU | — |
| 6 (nanoGPT até ~20M parâmetros) | Sim | — |
| 6 (reproduzir GPT-2 124M) | Não | Kaggle (~30 h de GPU/semana) ou Colab |
| 7 (QLoRA em 7–8B) | Não (só até ~1B) | Colab ou Kaggle com T4 de 16 GB |
| 7 (Ollama) | Sim | 7–8B quantizados rodam devagar na CPU |
| 7 (vLLM, teste de carga) | Não | GPU alugada por hora (RunPod, Vast.ai) |

## Resumo: o essencial de cada fase

| Fase | Leitura | Curso | Exercício central |
| --- | --- | --- | --- |
| 1. História | Melanie Mitchell | — | perceptron falhando no XOR |
| 2. IA clássica | Russell & Norvig; Sutton & Barto | CS50 AI | A* e Q-learning |
| 3. Matemática | Mathematics for ML | 3Blue1Brown | regressão linear com gradiente descendente |
| 4. ML clássico | ISLP | Andrew Ng | 5 modelos + análise de erros |
| 5. Deep learning | d2l.ai | Karpathy, Zero to Hero | micrograd |
| 6. Transformers | Raschka | Karpathy, *Let's build GPT* | nanoGPT + ablação |
| 7. Aplicação | Chip Huyen | Hugging Face LLM e Agents | RAG + eval |
| 8. Projeto final | — | — | assistente de negociação + reprodução de paper |

Os livros de Raschka, Huyen, Géron, Alammar, Mitchell e Metz são pagos; os demais têm versão online gratuita. Confira a edição mais recente antes de comprar.
