#!/usr/bin/env python3
"""Create a dated report for public GitHub sources referenced by the catalog."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
GITHUB_RE = re.compile(
    r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)(?:[/?#)\s]|$)"
)


def fetch(owner: str, repo: str) -> dict[str, object]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "about-my-tool-box-freshness/2.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com/repos/{owner}/{repo}", headers=headers)
    try:
        with urlopen(request, timeout=20) as response:
            data = json.load(response)
        license_data = data.get("license") or {}
        return {
            "status": "ok",
            "canonical": data.get("full_name", f"{owner}/{repo}"),
            "visibility": data.get("visibility", "?"),
            "license": license_data.get("spdx_id", "não declarada"),
            "pushed": data.get("pushed_at", "?"),
            "archived": data.get("archived", False),
            "disabled": data.get("disabled", False),
            "fork": data.get("fork", False),
            "url": data.get("html_url", f"https://github.com/{owner}/{repo}"),
        }
    except HTTPError as exc:
        return {"status": f"http-{exc.code}"}
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        return {"status": "erro", "detail": str(exc)}


def referenced_repositories() -> list[tuple[str, str]]:
    text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((ROOT / "catalog").glob("*.md"))
    )
    return sorted(set(GITHUB_RE.findall(text)), key=lambda item: (item[0].lower(), item[1].lower()))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="reports/catalog-freshness.md")
    args = parser.parse_args()

    repos = referenced_repositories()
    rows = [
        "# Relatório de atualidade do catálogo",
        "",
        (
            f"Gerado em {datetime.now(timezone.utc).isoformat()}. "
            "O relatório confirma metadados públicos; não prova qualidade, segurança ou E3."
        ),
        "",
        "| Fonte solicitada | Fonte canônica | Estado | Visibilidade | Licença GitHub | Último push | Arquivado | Fork |",
        "|---|---|---|---|---|---|---:|---:|",
    ]
    problems = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = list(executor.map(lambda item: fetch(*item), repos))

    for (owner, repo), result in zip(repos, results):
        status = str(result.get("status", "?"))
        canonical = str(result.get("canonical", "?"))
        visibility = str(result.get("visibility", "?"))
        renamed = canonical.lower() != f"{owner}/{repo}".lower()
        if (
            status != "ok"
            or visibility != "public"
            or result.get("archived")
            or result.get("disabled")
            or renamed
        ):
            problems += 1
        canonical_url = str(result.get("url", f"https://github.com/{owner}/{repo}"))
        rows.append(
            "| "
            f"[{owner}/{repo}](https://github.com/{owner}/{repo}) | "
            f"[{canonical}]({canonical_url}) | {status} | "
            f"{visibility} | {result.get('license', '?')} | "
            f"{result.get('pushed', '?')} | {result.get('archived', '?')} | "
            f"{result.get('fork', '?')} |"
        )

    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(rows) + "\n", encoding="utf-8")
    display_output = output.relative_to(ROOT) if output.is_relative_to(ROOT) else output
    print(
        f"Relatório criado: {display_output} "
        f"({len(repos)} repositórios, {problems} sinais para revisão)"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
