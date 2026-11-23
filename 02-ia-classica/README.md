# Fase 2 — IA clássica: lógica, busca, sistemas especialistas e RL (mês 2)

**Objetivo:** dominar as técnicas anteriores ao deep learning que continuam dentro de sistemas modernos.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## Como estudar esta fase

Curso principal: **CS50 AI** (Harvard), [cs50.harvard.edu/ai](https://cs50.harvard.edu/ai/). Assista à aula, leia o capítulo do Russell & Norvig e implemente sem olhar soluções prontas. Os *projects* do CS50 AI são ótimos exercícios [C].

## Semana a semana

| Semana | Tópicos | Estudar | Praticar |
| --- | --- | --- | --- |
| 1 | Espaço de estados, BFS, DFS, custo uniforme, busca gulosa, A*, heurística admissível e consistente | CS50 AI, aula 0 (*Search*); Russell & Norvig, cap. 3 | [O] labirinto com BFS/DFS/A* · experimento de heurísticas |
| 2 | Busca adversarial: minimax, poda alfa-beta, profundidade limitada; CSP: backtracking, propagação de restrições | CS50 AI, aula 0 (parte de jogos) e aula 3 (*Optimization*, parte de CSP); Russell & Norvig, caps. 5 e 6 | [O] jogo da velha com minimax e alfa-beta · [C] Sudoku como CSP |
| 3 | Lógica proposicional, model checking, inferência, lógica de primeira ordem, base de conhecimento, encadeamento para frente e para trás | CS50 AI, aula 1 (*Knowledge*); Russell & Norvig, caps. 7–9 (leia 7 inteiro; 8–9 por cima) | [O] sistema especialista de elegibilidade de acordo |
| 4 | RL: agente, ambiente, recompensa, MDP, política, função de valor, exploração × aproveitamento, bandits, Q-learning | Sutton & Barto, caps. 1, 2 (bandits), 3 (MDP) e 6.5 (Q-learning) — [livro gratuito](http://incompleteideas.net/book/the-book-2nd.html); [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course), unidades 1–2 [C] | [O] Q-learning no FrozenLake · [C] bandit ε-greedy × UCB · avaliação |

## Sugestões

- Implemente BFS, DFS e A* com a **mesma interface** (fila, pilha, fila de prioridade). Assim a diferença entre eles fica evidente no código.
- No sistema especialista, use regras do seu domínio (fictícias): você vai sentir na prática por que regras escritas à mão entram em conflito e não escalam, que é a lição da Fase 1.
- No Q-learning, imprima a tabela Q a cada 1000 episódios. Ver os valores se propagando a partir do objetivo é o melhor jeito de entender RL.
- Guarde o Q-learning: ele volta na Fase 7, como base do RLHF.
- [A] Monte Carlo Tree Search no Connect Four é a ideia central do AlphaGo sem a rede neural.

## Pronto para a avaliação quando

- Explica por que A* com heurística admissível acha o caminho ótimo.
- Implementa A* e Q-learning do zero e interpreta a curva de recompensa.
