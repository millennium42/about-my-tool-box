#!/usr/bin/env python3
"""Validate the repository's documentation, internal links and optional URLs."""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "catalog/tools.md",
    "catalog/mcp-servers.md",
    "guides/verification.md",
    "projects/spec-template.md",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"https?://[^\s`\)\]]*[<][^\s`\)\]]*[>]")
PRIVATE_PATH_RE = re.compile(r"(?:[A-Za-z]:\\Users\\(?:[^\\\s]+)|/home/[^/\s]+)")


def markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md") if ".git" not in p.parts
    )


def external_links() -> list[tuple[Path, str]]:
    links: list[tuple[Path, str]] = []
    for path in markdown_files():
        for match in LINK_RE.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1).strip().strip("<>")
            if target.startswith(("http://", "https://")):
                links.append((path, target))
    return sorted(set(links))


def check_local_links(errors: list[str]) -> int:
    count = 0
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "#")):
                continue
            target = target.split("#", 1)[0]
            target = target.split("?", 1)[0]
            if not target:
                continue
            count += 1
            destination = (path.parent / target).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f"link interno inexistente: {path.relative_to(ROOT)} -> {target}")
    return count


def check_content(errors: list[str]) -> None:
    for relative in REQUIRED:
        if not (ROOT / relative).exists():
            errors.append(f"arquivo obrigatório ausente: {relative}")

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if PLACEHOLDER_RE.search(text):
            errors.append(f"URL placeholder encontrada: {path.relative_to(ROOT)}")
        if PRIVATE_PATH_RE.search(text):
            errors.append(f"caminho pessoal encontrado: {path.relative_to(ROOT)}")

    tools = (ROOT / "catalog/tools.md").read_text(encoding="utf-8")
    for status in ("Verificada", "Em avaliação", "Referência", "Arquivada"):
        if status not in tools:
            errors.append(f"status ausente no catálogo: {status}")
    if "Somente E3" not in (ROOT / "guides/verification.md").read_text(encoding="utf-8"):
        errors.append("critério E3 não está declarado")


def request_status(url: str) -> tuple[int | None, str | None]:
    headers = {"User-Agent": "about-my-tool-box-link-check/1.0"}
    for method in ("HEAD", "GET"):
        try:
            request = Request(url, method=method, headers=headers)
            with urlopen(request, timeout=20) as response:
                return response.status, None
        except HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405):
                continue
            return exc.code, None
        except (URLError, TimeoutError, OSError) as exc:
            if method == "HEAD":
                continue
            return None, str(exc)
    return None, "sem resposta"


def check_network(errors: list[str], warnings: list[str]) -> int:
    checked = 0
    for path, url in external_links():
        parsed = urlparse(url)
        if parsed.hostname in {"localhost", "127.0.0.1", "::1"}:
            continue
        checked += 1
        status, problem = request_status(url)
        # Alguns sites bloqueiam clientes automatizados com 401/403/405 sem
        # significar que a documentação deixou de existir. 404 e falhas de
        # rede continuam sendo erros reais para o catálogo.
        if status in {401, 403, 405}:
            warnings.append(f"acesso automatizado restrito: {path.relative_to(ROOT)} -> {url} [{status}]")
        elif status is None or status >= 400:
            suffix = f" ({problem})" if problem else ""
            errors.append(f"link externo indisponível: {path.relative_to(ROOT)} -> {url} [{status}]{suffix}")
        time.sleep(0.05)
    return checked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--network", action="store_true", help="also check external URLs")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    local_count = check_local_links(errors)
    check_content(errors)
    external_count = check_network(errors, warnings) if args.network else 0

    print(f"Arquivos Markdown: {len(markdown_files())}")
    print(f"Links internos verificados: {local_count}")
    if args.network:
        print(f"Links externos verificados: {external_count}")
        if warnings:
            print(f"Avisos de acesso restrito: {len(warnings)}")
            for warning in warnings:
                print(f"- {warning}")
    if errors:
        print(f"Falhas: {len(errors)}")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Verificação concluída sem falhas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
