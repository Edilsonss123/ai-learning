#!/usr/bin/env python3
"""Lê os PROGRESSO.md de cada fase e o histórico do git e gera site/progress.json.

Uso:  python scripts/build_progress.py
Só usa a biblioteca padrão do Python 3.9+.
"""
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "progress.json"
CHECK = re.compile(r"^\s*[-*]\s+\[( |x|X)\]\s+(?:\[([^\]]+)\]\s+)?(.+?)\s*$")
DIARIO = re.compile(r"^\s*[-*]\s+(\d{4}-\d{2}-\d{2})\s*[:\-–]\s*(.+?)\s*$")


def git(*args):
    try:
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True)
        return r.stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def commits(caminho=None, limite=None):
    args = ["log", "--no-merges", "--format=%h%x1f%aI%x1f%s"]
    if limite:
        args.append(f"-n{limite}")
    if caminho:
        args += ["--", caminho]
    raiz = set(git("rev-list", "--max-parents=0", "HEAD").split())
    out = []
    for linha in git(*args).splitlines():
        partes = linha.split("\x1f")
        if len(partes) == 3 and not any(r.startswith(partes[0]) for r in raiz if caminho):
            out.append({"hash": partes[0], "data": partes[1], "msg": partes[2]})
    return out


def ler_progresso(arquivo):
    secoes, diario, atual = {}, [], None
    if not arquivo.exists():
        return secoes, diario
    for linha in arquivo.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## "):
            atual = linha[3:].strip()
            continue
        if atual is None:
            continue
        if atual.lower().startswith("di"):
            m = DIARIO.match(linha)
            if m:
                diario.append({"data": m.group(1), "texto": m.group(2)})
            continue
        m = CHECK.match(linha)
        if m:
            secoes.setdefault(atual, []).append({
                "feito": m.group(1).lower() == "x",
                "nivel": (m.group(2) or "").strip(),
                "texto": m.group(3),
            })
    return secoes, diario


def url_repo():
    remoto = git("config", "--get", "remote.origin.url").strip()
    if not remoto:
        return ""
    remoto = re.sub(r"^git@github\.com:", "https://github.com/", remoto)
    return re.sub(r"\.git$", "", remoto)


def main():
    trilha = json.loads((ROOT / "trilha.json").read_text(encoding="utf-8"))
    fases = []
    for f in trilha["fases"]:
        pasta = ROOT / f["pasta"]
        secoes, diario = ler_progresso(pasta / "PROGRESSO.md")
        cs = commits(f["pasta"])
        arquivos = sorted(
            str(p.relative_to(pasta)).replace("\\", "/")
            for p in pasta.rglob("*") if p.is_file() and p.name != "PROGRESSO.md"
        ) if pasta.exists() else []
        fases.append({**f, "secoes": secoes, "diario": sorted(diario, key=lambda d: d["data"], reverse=True),
                      "commits": cs[:30], "total_commits": len(cs), "arquivos": arquivos[:60],
                      "tem_experimento": any(a.upper().endswith("EXPERIMENTO.MD") for a in arquivos)})

    semanas = {}
    for c in commits():
        dia = datetime.fromisoformat(c["data"]).date()
        seg = dia.fromordinal(dia.toordinal() - dia.weekday()).isoformat()
        semanas[seg] = semanas.get(seg, 0) + 1

    dados = {
        "gerado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "repo": url_repo(),
        "inicio": trilha.get("inicio"),
        "horas_semana": trilha.get("horas_semana", 8),
        "fases": fases,
        "commits_por_semana": semanas,
        "ultimos_commits": commits(limite=15),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
    feitos = sum(i["feito"] for f in fases for s in f["secoes"].values() for i in s)
    total = sum(len(s) for f in fases for s in f["secoes"].values())
    print(f"{OUT.relative_to(ROOT)}: {feitos}/{total} itens concluídos")


if __name__ == "__main__":
    main()
