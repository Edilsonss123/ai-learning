# Fase 5 — Redes neurais e deep learning (meses 6–7)

**Objetivo:** escrever o backpropagation à mão antes de usar PyTorch. São 8 semanas; as 4 primeiras só para redes e backprop.
O que vou aprender e materiais: [REFERENCIAS.md](REFERENCIAS.md) · Exercícios e progresso: [PROGRESSO.md](PROGRESSO.md) · Visão geral: [PLANO.md](../PLANO.md)

## Como estudar esta fase

Curso principal da trilha: **Neural Networks: Zero to Hero**, de Andrej Karpathy ([karpathy.ai/zero-to-hero.html](https://karpathy.ai/zero-to-hero.html)).
Método: assista ao vídeo inteiro uma vez, depois **reescreva o código do zero com o vídeo fechado**. Volte ao vídeo só quando travar.
Livro de apoio: *Dive into Deep Learning* ([d2l.ai](https://d2l.ai/), gratuito, com código PyTorch).

## Semana a semana

| Semana | Tópicos | Estudar | Praticar |
| --- | --- | --- | --- |
| 1 | Neurônio, pesos, bias, ativações (sigmoid, tanh, ReLU), forward pass, perdas | d2l, caps. 3 (redes lineares) e 5.1 (MLP); 3Blue1Brown, série *Neural Networks*, vídeos 1–2 | [O] rede de 2 camadas resolvendo XOR |
| 2 | Backpropagation, grafo computacional, autograd | Karpathy, vídeo 1 (*micrograd*); 3Blue1Brown, *Neural Networks*, vídeos 3–4 (backprop) | [O] reescrever o micrograd · [O] gradient checking |
| 3 | SGD, momentum, Adam, inicialização, gradientes que somem ou explodem | Karpathy, vídeo 2 (*makemore* bigram) e vídeo 3 (*makemore* MLP); d2l, cap. 12 (otimização), seções de SGD, momentum e Adam | [O] makemore, partes 1–2 |
| 4 | PyTorch: tensores, `nn.Module`, `DataLoader`, loop de treino, GPU | Tutorial oficial *Learn the Basics* do PyTorch; d2l, cap. 6 (*Builders' Guide*) | [O] MLP no MNIST acima de 98% |
| 5 | BatchNorm, LayerNorm, dropout, learning rate schedule, diagnóstico de curvas | Karpathy, vídeo 4 (*activations, gradients, BatchNorm*) e vídeo 5 (*backprop ninja*); d2l, caps. 5.6 (dropout) e 8.5 (batch norm) | [O] makemore, partes 3–5 · experimento com e sem residual |
| 6 | CNNs: convolução, padding, stride, pooling, LeNet → AlexNet → VGG → ResNet | d2l, caps. 7 (CNN) e 8 (CNNs modernas: 8.1 AlexNet, 8.6 ResNet); paper da ResNet (He et al., 2015) | [O] CNN no Fashion-MNIST ou CIFAR-10 · experimento MLP × CNN |
| 7 | RNN, LSTM, GRU, backprop no tempo, por que perderam para o Transformer | d2l, caps. 9 (RNN) e 10 (LSTM, GRU); Karpathy, vídeo 6 (*WaveNet*) [C] | [C] RNN de caracteres em português |
| 8 | Embeddings (word2vec), Seq2Seq, encoder-decoder, primeira atenção (Bahdanau) | d2l, caps. 10.7 (Seq2Seq) e 11.1–11.4 (atenção); Jay Alammar, *The Illustrated Word2vec* | [C] fine-tuning de ResNet · análise de erros · avaliação |

## Sugestões

- A semana 2 é a mais importante da trilha inteira. Se o micrograd não ficar claro, repita a semana.
- Faça o *backprop ninja* (vídeo 5) com calma: é onde o backprop deixa de ser mágica.
- Sempre plote as curvas de perda de treino e de validação juntas. Diagnosticar curvas é a habilidade cobrada em "Analisar".
- Use a GPU local (4 GB) para MNIST e CIFAR. Para fine-tuning da ResNet, o Colab basta.
- [C] fast.ai (*Practical Deep Learning for Coders*): ótimo se quiser ver resultados rápidos antes do detalhe.
- [C] *Understanding Deep Learning* (Simon Prince, gratuito): as melhores figuras para entender cada conceito.

## Pronto para a avaliação quando

- Explica o backprop de uma rede de 2 camadas no quadro.
- Treina uma rede do zero em NumPy e diagnostica uma curva com overfitting ou gradiente sumindo.
