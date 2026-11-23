# Fase 7 — Pós-treino, RAG, agentes e produção (meses 10–11)

**Objetivo:** transformar um modelo base em assistente e construir sistemas confiáveis sobre LLMs, com avaliação e segurança.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## Como estudar esta fase

Leitura principal: **AI Engineering**, de Chip Huyen. Ela organiza a fase inteira: avaliação, prompt, RAG, agentes, fine-tuning, inferência.
Prática: Hugging Face LLM Course ([huggingface.co/learn/llm-course](https://huggingface.co/learn/llm-course)) e Agents Course ([huggingface.co/learn/agents-course](https://huggingface.co/learn/agents-course)).
Aqui o seu lado .NET pesa a favor: sempre que possível, implemente a parte de sistema em C#.

## Semana a semana

| Semana | Tópicos | Estudar | Praticar |
| --- | --- | --- | --- |
| 1 | SFT: dados de instrução, formato de chat, por que o modelo base não conversa | Raschka, *Build a LLM from Scratch*, cap. 7 (instruction fine-tuning); Huyen, cap. 2 (pós-treino) | montar o dataset de 200 instruções |
| 2 | RLHF (modelo de recompensa + PPO), DPO, Constitutional AI; ligação com o Q-learning da Fase 2 | Paper *InstructGPT* (Ouyang et al., 2022); paper *DPO* (Rafailov et al., 2023), resumo e método; Huyen, cap. 2 | [A] DPO com pares próprios |
| 3 | LoRA, QLoRA, PEFT; quando fazer fine-tuning × quando usar só prompt | Huyen, caps. 7 (finetuning) e 8 (dataset engineering); paper *LoRA* (Hu et al., 2021); Hugging Face LLM Course, capítulos de fine-tuning | [O] QLoRA no Colab ou Kaggle |
| 4 | Prompt engineering: few-shot, chain-of-thought, saídas estruturadas (JSON), system prompts | Huyen, cap. 5; [Anthropic Courses](https://github.com/anthropics/courses), *Prompt engineering interactive tutorial* [C] | baseline de prompt para o experimento final |
| 5 | RAG: chunking, embeddings, bancos vetoriais (pgvector, Qdrant), busca híbrida (BM25 + vetor), reranking | Huyen, cap. 6 (RAG); paper *RAG* (Lewis et al., 2020); DeepLearning.AI Short Courses sobre RAG [C] | [O] RAG do zero com pgvector |
| 6 | Agentes: tool calling, planejamento, ReAct, memória, MCP | Huyen, cap. 6 (agentes); paper *ReAct* (Yao et al., 2022); Hugging Face Agents Course, unidades 1–2; especificação do MCP ([modelcontextprotocol.io](https://modelcontextprotocol.io/)) | [O] agente em C# · [C] servidor MCP em .NET |
| 7 | Avaliação: conjuntos de teste, métricas por tarefa, LLM-como-juiz, regressão de qualidade | Huyen, caps. 3 e 4 (avaliação) | [O] eval com 100 perguntas · experimentos de ablação do RAG |
| 8 | Produção: latência, custo por token, cache, batching, quantização, observabilidade; Ollama e vLLM | Huyen, caps. 9 (inferência) e 10 (arquitetura); documentação do Ollama e do vLLM | [C] Ollama: p50, p95, tokens/s |
| 9 | Segurança: alucinação, prompt injection, vazamento de dados, LGPD, permissões e auditoria | Huyen, cap. 5 (defesas contra prompt injection) e cap. 10; OWASP *Top 10 for LLM Applications* | [O] atacar o próprio agente · avaliação |

## Sugestões

- **Avaliação primeiro:** monte o eval (semana 7) cedo, de forma simples, e use-o para medir cada mudança desde a semana 3.
- Faça o RAG **sem framework** primeiro (LangChain, Semantic Kernel e similares escondem as decisões que você precisa entender). Use framework só depois, se quiser.
- QLoRA de modelos 7–8B não cabe na sua GPU de 4 GB: use Colab ou Kaggle (T4 de 16 GB).
- Anote o custo (tokens e dólares) de cada experimento. Isso vira argumento no projeto final.
- [C] *Hands-On Large Language Models* (Alammar e Grootendorst): ótimo para visualizar embeddings e RAG.

## Pronto para a avaliação quando

- Explica SFT × RLHF × DPO e quando usar RAG em vez de fine-tuning.
- Tem RAG e agente funcionando sem orquestrador, e um relatório de eval que aponta a causa principal das falhas.
