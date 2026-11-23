# Fase 3 — Matemática para IA (meses 3–4)

**Objetivo:** ler qualquer fórmula de rede neural e implementá-la em NumPy. São 8 semanas.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## Como estudar esta fase

Sempre nesta ordem: **intuição visual → leitura → código**.
1. Vídeo do 3Blue1Brown (intuição).
2. Capítulo do *Mathematics for Machine Learning* ([mml-book.github.io](https://mml-book.github.io/), gratuito).
3. Implementar em Python puro e depois em NumPy.
4. Khan Academy em português ([pt.khanacademy.org](https://pt.khanacademy.org/)) só para tapar buracos.

## Semana a semana

| Semana | Tópicos | Estudar | Praticar |
| --- | --- | --- | --- |
| 1 | Vetores, combinação linear, produto escalar, norma, similaridade de cosseno | 3Blue1Brown, *Essence of Linear Algebra*, caps. 1–2 e 9 (produto escalar); MML, cap. 2 (2.1–2.4) e 3.1–3.4 | [O] vetores em Python puro × NumPy |
| 2 | Matriz como transformação linear, multiplicação, transposta, inversa, determinante | *Essence of Linear Algebra*, caps. 3–7; MML, cap. 2 (2.2–2.7) | [O] multiplicação de matrizes do zero |
| 3 | Autovalores, autovetores, mudança de base, SVD, tensores | *Essence of Linear Algebra*, caps. 13–14; MML, cap. 4 (4.2, 4.4, 4.5) | [C] compressão de imagem com SVD |
| 4 | Limite, derivada, derivada parcial, gradiente | 3Blue1Brown, *Essence of Calculus*, caps. 1–4; MML, cap. 5 (5.1–5.2) | [O] derivadas numéricas × analíticas |
| 5 | Regra da cadeia, gradiente de funções vetoriais, jacobiano, grafo computacional | *Essence of Calculus*, cap. 4 (regra da cadeia); MML, cap. 5 (5.3–5.6, backprop e diferenciação automática) | [O] gradiente descendente em f(x, y) = x² + 3y² |
| 6 | Probabilidade condicional, Bayes, variáveis aleatórias, Bernoulli, categórica, normal, esperança, variância | MML, cap. 6 (6.1–6.5); 3Blue1Brown, vídeo sobre o teorema de Bayes | [C] simulação de dados × teoria |
| 7 | Máxima verossimilhança, entropia, entropia cruzada, divergência KL | MML, cap. 8 (8.3, máxima verossimilhança); busque também uma explicação visual de entropia cruzada | [O] entropia cruzada à mão e em código |
| 8 | Função de perda, gradiente descendente, taxa de aprendizado, SGD, momentum, convexidade | MML, cap. 7 (7.1–7.3) | [O] regressão linear do zero · experimento de taxa de aprendizado · avaliação |

## Sugestões

- **Não tente provar teoremas.** O objetivo é saber o que cada operação faz e conseguir programá-la.
- Para cada fórmula nova, escreva a versão em NumPy logo abaixo da fórmula nas suas notas.
- Shapes são metade do trabalho: anote o formato (shape) de cada matriz em todo exercício.
- Se travar no cálculo, volte ao vídeo; se travar na notação, volte ao MML.
- [C] Curso guiado: *Mathematics for Machine Learning and Data Science*, da DeepLearning.AI (Coursera).

## Pronto para a avaliação quando

- Explica o gradiente e a regra da cadeia sem notas.
- Treina uma regressão linear com gradiente descendente do zero e explica por que η alto diverge.
