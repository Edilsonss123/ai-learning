# Referências — Fase 5: Redes neurais e deep learning

## O que você vai aprender

- O que uma rede neural calcula: neurônios, camadas, ativações e funções de perda.
- **Backpropagation** de verdade: grafo computacional, regra da cadeia e autograd, implementados do zero (micrograd).
- Otimizadores (SGD, momentum, Adam), inicialização e o problema dos gradientes que somem ou explodem.
- **PyTorch**: tensores, `nn.Module`, `DataLoader`, loop de treino e GPU.
- Técnicas de treino: BatchNorm, LayerNorm, dropout, learning rate schedule e diagnóstico de curvas.
- **CNNs** (convolução, pooling, ResNet e conexões residuais) para imagens.
- **RNN, LSTM e GRU** para sequências, e por que foram substituídas pelo Transformer.
- **Embeddings**, Seq2Seq e a primeira forma de atenção, a ponte para a Fase 6.

## Material principal

| Material | Tipo | Onde usar |
| --- | --- | --- |
| [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — Andrej Karpathy | curso em vídeo | vídeos 1–6 |
| [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) (gratuito) | livro | caps. 3, 5–12 |
| [Tutoriais oficiais do PyTorch](https://pytorch.org/tutorials/) | tutorial | semana 4 |
| 3Blue1Brown, série *Neural Networks* | vídeo | semanas 1–2 |

## Materiais alternativos

**Livros**
- [*Neural Networks and Deep Learning*](http://neuralnetworksanddeeplearning.com/) — Michael Nielsen (gratuito): a explicação mais clara de backprop já escrita.
- *Understanding Deep Learning* — Simon Prince (gratuito): as melhores figuras da área. [C]
- [*Deep Learning*](https://www.deeplearningbook.org/) — Goodfellow, Bengio, Courville: a referência teórica, para consulta por capítulo. [C]
- *Grokking Deep Learning* — Andrew Trask: redes do zero em NumPy, bem didático.
- *Deep Learning with Python* — François Chollet: abordagem prática com Keras.

**Cursos**
- [Practical Deep Learning for Coders](https://course.fast.ai/) — fast.ai: de cima para baixo, resultados rápidos. [C]
- *Deep Learning Specialization* — Andrew Ng (Coursera): ritmo guiado, com quizzes.
- **Stanford CS231n** (notas gratuitas em cs231n.github.io): a melhor referência sobre CNNs.
- **MIT 6.S191** (*Introduction to Deep Learning*, YouTube): panorama compacto e atualizado anualmente.

**Leituras curtas**
- Chris Olah, *Understanding LSTM Networks* (blog): a explicação clássica das LSTMs.
- Jay Alammar, *The Illustrated Word2vec*: embeddings de forma visual.
- Andrej Karpathy, *A Recipe for Training Neural Networks* (blog): como treinar sem se perder.
