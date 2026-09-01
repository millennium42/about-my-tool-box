#!/usr/bin/env python3
"""Create a dated GitHub-source freshness report for the catalog."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
GITHUB_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)(?:[/?#)\s]|$)")


def fetch(owner: str, repo: str) -> dict[str, object]:
    request = Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "about-my-tool-box-freshness/1.0"},
    )
    try:
        with urlopen(request, timeout=20) as response:
            data = json.load(response)
        return {
            "status": "ok",
            "stars": data.get("stargazers_count", "?"),
            "updated": data.get("pushed_at", "?"),
            "archived": data.get("archived", False),
            "url": data.get("html_url", f"https://github.com/{owner}/{repo}"),
        }
    except HTTPError as exc:
        return {"status": f"http-{exc.code}"}
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        return {"status": "erro", "detail": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="reports/catalog-freshness.md")
    args = parser.parse_args()

    text = (ROOT / "catalog/tools.md").read_text(encoding="utf-8")
    repos = sorted(set(GITHUB_RE.findall(text)))
    rows: list[str] = []
    rows.append("# Relatório de atualidade do catálogo")
    rows.append("")
    rows.append(f"Gerado em {datetime.now(timezone.utc).isoformat()}. Este relatório é um sinal de manutenção, não uma recomendação automática.")
    rows.append("")
    rows.append("| Repositório | Estado | Estrelas no momento | Último push | Arquivado |")
    rows.append("|---|---:|---:|---|---:|")
    for owner, repo in repos:
        result = fetch(owner, repo)
        rows.append(
            f"| [{owner}/{repo}](https://github.com/{owner}/{repo}) | {result.get('status', '?')} | {result.get('stars', '?')} | {result.get('updated', '?')} | {result.get('archived', '?')} |"
        )

    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"Relatório criado: {output.relative_to(ROOT)} ({len(repos)} repositórios GitHub)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
