# ai-learning

Minha trilha de 12 meses para me tornar especialista em IA: história → teoria → matemática → implementação → experimentação → aplicação real.

- **Plano completo:** [`PLANO.md`](PLANO.md)
- **Regras de organização (e instruções para o Claude):** [`CLAUDE.md`](CLAUDE.md)
- **Modelos:** [`templates/`](templates/) para experimento, ficha de paper, avaliação e nota
- **Cronograma (documento no Claude):** https://claude.ai/artifact/8385xjtBZqTsr5ie7Qw8yK
- **Painel de progresso (artefato no Claude):** https://claude.ai/artifact/Bo1xRAdw4wwQGoLKdHxULh, atualizado quando você pede ao Claude "atualize meu progresso"

## Como funciona

```text
ai-learning/
├── PLANO.md                 # cronograma completo
├── CLAUDE.md                # onde guardar cada coisa + papel do Claude
├── templates/               # EXPERIMENTO, PAPER, AVALIACAO, NOTA
├── trilha.json              # data de início e fases (edite "inicio")
├── 01-historia/
│   ├── PROGRESSO.md         # checklist da fase + diário de estudo
│   ├── EXPERIMENTO.md       # um por experimento (opcional, o painel detecta)
│   └── ...                  # seu código, notebooks, notas
├── 02-ia-classica/ … 08-projeto-final/
├── scripts/build_progress.py   # lê PROGRESSO.md + git log → site/progress.json
├── site/index.html             # o painel
└── .github/workflows/painel.yml
```

A cada push, a Action roda `build_progress.py`, que:

- conta os itens `- [x]` de cada `PROGRESSO.md` por nível: **[O]** obrigatório, **[C]** complementar, **[A]** avançado;
- lê a seção **Avaliação** (`[Explicar]`, `[Implementar]`, `[Analisar]`): a fase só conta como concluída com todos os obrigatórios e as três capacidades marcados;
- lê o **Diário** (`- 2026-12-03: estudei ELIZA e Dartmouth`);
- usa o `git log` de cada pasta: número de commits, último commit, arquivos e commits por semana;
- compara com o plano a partir de `inicio` em `trilha.json` (adiantado, no prazo ou atrasado).

## Configurar (uma vez)

1. Crie um repositório no GitHub chamado `ai-learning` e envie esta pasta:
   ```bash
   git init -b main
   git add .
   git commit -m "Início da trilha"
   git remote add origin https://github.com/SEU_USUARIO/ai-learning.git
   git push -u origin main
   ```
2. No GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Ajuste `"inicio"` em `trilha.json` para o dia em que você começar.
4. O painel fica em `https://SEU_USUARIO.github.io/ai-learning/`.

**Repositório privado (situação atual):** o GitHub Pages está desligado, porque no plano gratuito ele só publica repositórios públicos. O workflow `painel.yml` roda só manualmente. O painel fica no artefato do Claude (link acima) ou localmente. Para voltar ao Pages: torne o repositório público (ou assine o Pro) e reative o gatilho `push` no workflow.

## Rotina

```bash
# estudou algo: marque [x] no PROGRESSO.md da fase e anote no Diário
git add 01-historia
git commit -m "Fase 1: perceptron em AND e OR"
git push            # o painel atualiza em ~1 minuto
```

## Ver o painel localmente

```bash
python scripts/build_progress.py
python -m http.server -d site 8000
# abra http://localhost:8000
```
