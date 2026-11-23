# Fase 1 — História da IA, primeiros modelos e fracassos (mês 1)

**Objetivo:** entender de onde vêm as ideias atuais, por que a IA passou por dois invernos e o que cada fracasso ensinou.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## Como estudar esta fase

1. Leia o material da semana (cerca de 2,5 h).
2. Em paralelo, aprenda Python nas semanas 1 e 2 (cerca de 1,5 h por semana).
3. Faça os exercícios [O] da semana; registre no Diário.
4. Escreva uma nota curta por semana em `notas/`: o que a época prometeu e o que entregou.

## Semana a semana

| Semana | Tópicos | Estudar | Praticar |
| --- | --- | --- | --- |
| 1 | McCulloch & Pitts (1943), Turing e o "jogo da imitação" (1950), Dartmouth (1956), IA simbólica | Russell & Norvig, cap. 1 (seções de história); Turing, *Computing Machinery and Intelligence* (1950, leia as objeções); Mitchell, parte 1 | Python: tutorial oficial, caps. 3–5 |
| 2 | Perceptron de Rosenblatt (1958), ELIZA (1966), regras × aprendizado | Rosenblatt (1958), resumo e figuras; Weizenbaum (1966), artigo do ELIZA; Mitchell, capítulo sobre redes neurais iniciais | NumPy: arrays, broadcasting · [O] ELIZA de regras · [O] perceptron AND/OR |
| 3 | Primeiro inverno: ALPAC (1966), *Perceptrons* e XOR (1969), Lighthill (1973). Sistemas especialistas (MYCIN, XCON), Quinta Geração, Cyc, colapso das Lisp machines (segundo inverno) | Russell & Norvig, cap. 1 (invernos e sistemas especialistas); Mitchell, capítulos sobre ciclos de hype; *Genius Makers* [C], primeiros capítulos | [O] perceptron falhando no XOR · [O] experimento de convergência |
| 4 | A retomada: backprop (1986), LeNet (1998), AlexNet (2012), AlphaGo, Transformer (2017), GPT-3, ChatGPT; fracassos recentes: Tay, Galactica, Google Flu Trends, Watson Health | *Genius Makers*, capítulos sobre AlexNet e DeepMind [C]; Mitchell, capítulos finais sobre limites; reportagens sobre Tay e Galactica | [C] linha do tempo técnica × comercial · avaliação |

## Sugestões

- Para cada fracasso, responda numa linha: **limite técnico** (o método não podia) ou **promessa comercial** (venderam mais do que existia)? Essa distinção é a avaliação "Explicar".
- O XOR é o fio condutor da trilha: você o vê falhar aqui e resolve na Fase 5, com uma camada oculta. Guarde o gráfico.
- Não se aprofunde em datas; foque em **por que** cada abordagem parou de escalar.
- Leitura extra [A]: *The Quest for Artificial Intelligence*, de Nils Nilsson, como referência de consulta.

## Pronto para a avaliação quando

- Consegue contar a história de 1943 a 2022 em 5 minutos, citando os dois invernos e suas causas.
- O perceptron roda do zero e você explica o gráfico de erro do XOR.
