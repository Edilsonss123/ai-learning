# Plano de estudos: de usuário a especialista em IA

12 meses, 8 fases, 8 a 10 horas por semana. A ordem segue uma formação progressiva: **história → teoria → matemática → implementação → experimentação → aplicação real**. Você só avança de fase depois de passar na avaliação do mês.

Este arquivo é a visão geral e as regras comuns a todas as fases. O conteúdo de cada fase fica na pasta dela (veja [Fases](#fases)). As regras de organização estão no [`CLAUDE.md`](CLAUDE.md).

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

## Fases

Cada fase é autocontida na sua pasta:

- `README.md`: plano semana a semana (tópicos, o que estudar, o que praticar) e sugestões.
- `REFERENCIAS.md`: o que você vai aprender, material principal e materiais alternativos.
- `PROGRESSO.md`: exercícios, experimentos, avaliação e diário (o painel lê este arquivo).

| Fase | Meses | Plano | Referências | Progresso |
| --- | --- | --- | --- | --- |
| 1. História da IA, primeiros modelos e fracassos | 1 | [README](01-historia/README.md) | [REFERENCIAS](01-historia/REFERENCIAS.md) | [PROGRESSO](01-historia/PROGRESSO.md) |
| 2. IA clássica: lógica, busca, sistemas especialistas e RL | 2 | [README](02-ia-classica/README.md) | [REFERENCIAS](02-ia-classica/REFERENCIAS.md) | [PROGRESSO](02-ia-classica/PROGRESSO.md) |
| 3. Matemática para IA | 3–4 | [README](03-matematica/README.md) | [REFERENCIAS](03-matematica/REFERENCIAS.md) | [PROGRESSO](03-matematica/PROGRESSO.md) |
| 4. Machine learning clássico | 5 | [README](04-ml-classico/README.md) | [REFERENCIAS](04-ml-classico/REFERENCIAS.md) | [PROGRESSO](04-ml-classico/PROGRESSO.md) |
| 5. Redes neurais e deep learning | 6–7 | [README](05-deep-learning/README.md) | [REFERENCIAS](05-deep-learning/REFERENCIAS.md) | [PROGRESSO](05-deep-learning/PROGRESSO.md) |
| 6. Transformers e LLMs por dentro | 8–9 | [README](06-transformers/README.md) | [REFERENCIAS](06-transformers/REFERENCIAS.md) | [PROGRESSO](06-transformers/PROGRESSO.md) |
| 7. Pós-treino, RAG, agentes e produção | 10–11 | [README](07-aplicacao/README.md) | [REFERENCIAS](07-aplicacao/REFERENCIAS.md) | [PROGRESSO](07-aplicacao/PROGRESSO.md) |
| 8. Projeto final e reprodução de paper | 12 | [README](08-projeto-final/README.md) | [REFERENCIAS](08-projeto-final/REFERENCIAS.md) | [PROGRESSO](08-projeto-final/PROGRESSO.md) |

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
