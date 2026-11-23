# Fase 4 — Machine learning clássico (mês 5)

**Objetivo:** dominar o ciclo dados → modelo → avaliação → análise de erros.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## Como estudar esta fase

Livro principal: **ISLP**, *An Introduction to Statistical Learning with Python* ([statlearning.com](https://www.statlearning.com/), gratuito). Cada capítulo tem um *lab* em Python: faça o lab e depois implemente o algoritmo do zero.
Curso de apoio: *Machine Learning Specialization*, de Andrew Ng (Coursera), cursos 1 e 2.

## Semana a semana

| Semana | Tópicos | Estudar | Praticar |
| --- | --- | --- | --- |
| 1 | Aprendizado supervisionado × não supervisionado, regressão × classificação, regressão logística, divisão treino/validação/teste | ISLP, caps. 2 e 4 (4.1–4.3); Andrew Ng, curso 1, semanas 1–3 | [O] regressão logística do zero × scikit-learn |
| 2 | Overfitting, viés × variância, regularização L1/L2, validação cruzada, vazamento de dados | ISLP, caps. 5 (5.1) e 6 (6.2); Andrew Ng, curso 2, semana 3 | [C] provocar e corrigir vazamento |
| 3 | k-NN, árvores de decisão, random forest, gradient boosting, SVM | ISLP, caps. 2.2.3 (k-NN), 8 (árvores, bagging, random forest, boosting) e 9 (SVM); documentação do XGBoost (*Introduction to Boosted Trees*) | [O] k-NN do zero · [O] comparar 5 algoritmos |
| 4 | Métricas: precisão, recall, F1, ROC-AUC, calibração; k-means, PCA; pipelines | ISLP, caps. 4.4 (métricas) e 12 (PCA, k-means); guia do scikit-learn sobre *Model evaluation* e *Pipelines* | [O] classificador de aceite · experimentos · avaliação |

## Sugestões

- Antes de treinar qualquer modelo, crie um **baseline burro** (sempre a classe majoritária). Se o seu modelo não vence o baseline, há algo errado.
- Em dados desbalanceados, olhe a **matriz de confusão** antes da acurácia, sempre.
- Para o classificador de aceite, gere os dados sintéticos com uma regra conhecida mais ruído. Assim você sabe qual é a resposta certa e consegue julgar o modelo.
- A análise de 20 erros um por um é o exercício que mais ensina na fase. Não pule.
- [C] Kaggle Learn ([kaggle.com/learn](https://www.kaggle.com/learn)): *Intro to ML* e *Intermediate ML*, curtos e práticos.
- [C] Géron, *Hands-On Machine Learning*, parte I: o melhor livro "mão na massa" de scikit-learn.

## Pronto para a avaliação quando

- Explica viés × variância e por que acurácia engana em dados desbalanceados.
- Implementa regressão logística e k-NN do zero e propõe uma melhoria a partir dos erros do modelo.
