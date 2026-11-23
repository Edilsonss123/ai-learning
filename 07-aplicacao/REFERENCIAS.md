# Referências — Fase 7: Pós-treino, RAG, agentes e produção

## O que você vai aprender

- Como um modelo base vira assistente: **SFT**, **RLHF** (com a ligação ao RL da Fase 2), **DPO** e Constitutional AI.
- **Fine-tuning eficiente** com LoRA e QLoRA, e quando ajustar o modelo em vez de só melhorar o prompt.
- **Prompt engineering** sério: few-shot, chain-of-thought e saídas estruturadas.
- **RAG**: chunking, embeddings, bancos vetoriais, busca híbrida e reranking, com citação de fontes.
- **Agentes**: tool calling, planejamento (ReAct), memória e o protocolo MCP.
- **Avaliação (evals)**: conjuntos de teste, LLM-como-juiz e regressão de qualidade.
- **Produção**: latência, custo por token, cache, observabilidade e servir modelos (Ollama, vLLM).
- **Segurança**: alucinação, prompt injection, vazamento de dados, LGPD, permissões e auditoria.

## Material principal

| Material | Tipo | Onde usar |
| --- | --- | --- |
| *AI Engineering* — Chip Huyen | livro | caps. 2–10, a fase inteira |
| *Build a Large Language Model (From Scratch)* — Raschka, caps. 6–7 | livro | semana 1 |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | curso | fine-tuning |
| [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) | curso | agentes |
| Papers: *InstructGPT*, *LoRA*, *DPO*, *RAG*, *ReAct* | paper | semanas 2, 3, 5, 6 |

## Materiais alternativos

**Livros**
- *Hands-On Large Language Models* — Alammar e Grootendorst: embeddings, RAG e fine-tuning com muitas figuras. [C]
- *LLM Engineer's Handbook* — Paul Iusztin e Maxime Labonne: do fine-tuning ao deploy, com projeto completo.
- *Designing Machine Learning Systems* — Chip Huyen: a parte de sistemas e MLOps.

**Cursos e guias**
- [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/): RAG, agentes, evals e fine-tuning em 1–2 h cada. [C]
- [Anthropic Courses](https://github.com/anthropics/courses): prompt engineering e tool use, com notebooks. [C]
- [Prompt Engineering Guide](https://www.promptingguide.ai/): referência de técnicas de prompt.
- [LLM Course](https://github.com/mlabonne/llm-course) — Maxime Labonne (GitHub): roteiro com notebooks de fine-tuning, quantização e RLHF.

**Ferramentas e documentação**
- [Unsloth](https://github.com/unslothai/unsloth): QLoRA rápido no Colab.
- [TRL](https://huggingface.co/docs/trl) (Hugging Face): SFT, DPO e PPO.
- [Semantic Kernel](https://learn.microsoft.com/semantic-kernel/) (Microsoft): agentes e RAG em C#.
- [Model Context Protocol](https://modelcontextprotocol.io/): especificação e SDK em C#.
- [pgvector](https://github.com/pgvector/pgvector): busca vetorial no PostgreSQL.

**Blogs**
- Anthropic, *Building effective agents*: padrões de agentes que funcionam em produção.
- Hamel Husain (hamel.dev): o melhor material prático sobre evals.
- Eugene Yan (eugeneyan.com): padrões para sistemas com LLM.
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/): segurança.
