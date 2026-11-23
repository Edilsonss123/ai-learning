# Referências — Fase 2: IA clássica — lógica, busca, sistemas especialistas e RL

## O que você vai aprender

- Modelar um problema como **espaço de estados** e resolvê-lo com BFS, DFS, custo uniforme e A*.
- Por que uma heurística admissível garante o caminho ótimo e como uma heurística melhor reduz o trabalho.
- Jogar de forma ótima com **minimax** e cortar a árvore com **poda alfa-beta**.
- Resolver problemas de restrição (CSP) com backtracking e propagação.
- Representar conhecimento em **lógica** e montar um **sistema especialista** com encadeamento para frente e para trás.
- Fundamentos de **aprendizado por reforço**: MDP, recompensa, política, exploração × aproveitamento, bandits e Q-learning tabular. É a base do RLHF da Fase 7.

## Material principal

| Material | Tipo | Onde usar |
| --- | --- | --- |
| [CS50's Introduction to AI with Python](https://cs50.harvard.edu/ai/) — Harvard (gratuito) | curso | aulas 0, 1 e 3 |
| *Inteligência Artificial: Uma Abordagem Moderna* — Russell & Norvig | livro | caps. 3, 5, 6, 7–9 |
| [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) — Sutton & Barto (gratuito) | livro | caps. 1, 2, 3 e 6.5 |
| [Gymnasium](https://gymnasium.farama.org/) | biblioteca | FrozenLake |

## Materiais alternativos

**Se preferir outro curso de IA clássica**
- **UC Berkeley CS188** (*Introduction to Artificial Intelligence*, [ai.berkeley.edu](https://ai.berkeley.edu/)): os famosos projetos do Pac-Man cobrem busca, jogos e RL. Excelente substituto ou complemento do CS50 AI.

**Para busca e A***
- [Red Blob Games, *Introduction to A**](https://www.redblobgames.com/pathfinding/a-star/introduction.html): explicação interativa, a melhor intuição visual disponível.

**Para lógica e sistemas especialistas**
- [*Learn Prolog Now!*](https://lpn.cs.uni-saarland.de/) (gratuito): para sentir uma linguagem feita para inferência lógica. [C]

**Para aprendizado por reforço**
- Curso de RL de **David Silver** (UCL/DeepMind, YouTube): aulas 1–5 cobrem MDP, programação dinâmica e Q-learning.
- [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course): prático, com notebooks. [C]
- *Grokking Deep Reinforcement Learning* — Miguel Morales: mais didático que o Sutton & Barto. [C]
- [OpenAI Spinning Up](https://spinningup.openai.com/): para RL profundo depois da trilha. [A]
