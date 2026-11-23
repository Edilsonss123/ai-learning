# Referências — Fase 8: Projeto final e reprodução de paper

## O que você vai aprender

- Transformar um problema de negócio (negociação de dívidas) em requisitos, métricas de sucesso e um baseline.
- Integrar num só sistema o que veio das fases anteriores: regras (Fase 2), classificador (Fase 4), RAG e agente (Fase 7).
- Provar com **eval** que o sistema é melhor que o baseline, e documentar quando não for.
- Testar segurança e desempenho antes de considerar algo pronto.
- **Reproduzir um paper**: escolher um resultado, replicá-lo em escala pequena e explicar as diferenças.
- Documentar decisões técnicas como portfólio: arquitetura, trade-offs, números e falhas.

## Material principal

| Material | Tipo | Onde usar |
| --- | --- | --- |
| *AI Engineering* — Chip Huyen, caps. 1, 4 e 10 | livro | planejamento, critérios de avaliação, arquitetura |
| [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | guia | testes de segurança |
| O paper escolhido + [`templates/PAPER.md`](../templates/PAPER.md) | paper | reprodução |

## Materiais alternativos

**Sistemas e arquitetura**
- *Designing Machine Learning Systems* — Chip Huyen: ciclo de vida de sistemas de ML em produção.
- *Designing Data-Intensive Applications* — Martin Kleppmann: fundamentos de sistemas de dados. [C]
- Blogs de engenharia de empresas que usam LLMs em produção: compare as arquiteturas que eles descrevem com a sua.

**Reprodução de papers**
- [Hugging Face Papers](https://huggingface.co/papers): papers recentes com código e modelos associados.
- Andrej Karpathy, *A Recipe for Training Neural Networks* (blog): como depurar quando o resultado não bate.
- Repositórios oficiais dos papers no GitHub: compare a sua implementação com a original só depois de tentar.

**Comunicação técnica**
- Posts técnicos de Simon Willison (simonwillison.net) e de Eugene Yan (eugeneyan.com): bons exemplos de como escrever sobre projetos de IA.
