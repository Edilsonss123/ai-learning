# Fase 8 — Projeto final e reprodução de paper (mês 12)

**Objetivo:** juntar as Fases 2 a 7 num **assistente de negociação de dívidas** e provar com métricas que ele funciona. Só dados fictícios.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## O que o sistema faz

1. Entende a pergunta do devedor (LLM).
2. Busca regras, políticas e ofertas (RAG, Fase 7).
3. Estima a chance de aceite de cada proposta (classificador, Fase 4).
4. Chama APIs de simulação de acordo por tool calling (agente, Fase 7).
5. É comparado com um baseline de regras (sistema especialista, Fase 2).

## Semana a semana

| Semana | Entrega | Reaproveite | Consultar |
| --- | --- | --- | --- |
| 1 | Problema, requisitos, métricas de sucesso, dataset sintético, baseline de regras | sistema especialista (Fase 2), gerador de dados (Fase 4) | Huyen, *AI Engineering*, cap. 1 (planejar uma aplicação) e cap. 4 (critérios de avaliação) |
| 2 | Backend .NET, RAG, classificador de aceite, agente com tools | RAG e agente (Fase 7), classificador (Fase 4) | Huyen, cap. 10 (arquitetura) |
| 3 | Eval com casos difíceis e de abuso, testes de segurança e de desempenho; comparação com o baseline | eval e ataques (Fase 7) | OWASP *Top 10 for LLM Applications* |
| 4 | README com arquitetura e decisões, post técnico, apresentação | — | — |

## Reprodução de paper (em paralelo, 2 h por semana)

Escolha **um** paper já lido na trilha e reproduza um resultado (uma tabela ou figura) em pequena escala. Sugestões, da mais simples para a mais difícil:

1. **LoRA** (Hu et al., 2021): qualidade × rank r em um modelo pequeno.
2. **Chinchilla** (Hoffmann et al., 2022): perda × tamanho do modelo com orçamento fixo de computação.
3. **ResNet** (He et al., 2015): rede profunda com e sem conexões residuais.
4. **Attention Is All You Need** (2017): ablação de cabeças e de posição.

Use a ficha [`templates/PAPER.md`](../templates/PAPER.md) e registre a reprodução como experimento (`exp01-repro-<slug>/`).

## Sugestões

- Defina as métricas de sucesso **antes** de escrever código (taxa de resposta correta, chance média de aceite das propostas, latência p95, custo por conversa).
- Comece pelo baseline de regras: se o sistema com LLM não o vencer no eval, isso também é um resultado. Documente.
- O README é a entrega principal para portfólio: diagrama de arquitetura, decisões com o porquê, números e o que falhou.

## Pronto para a avaliação final quando

- Explica cada decisão de arquitetura para um engenheiro sênior.
- Outra pessoa consegue rodar o sistema só seguindo o README.
- O relatório mostra eval, análise de erros e limitações.
