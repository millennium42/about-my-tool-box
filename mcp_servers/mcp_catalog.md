# Catálogo de MCP Servers

MCP (Model Context Protocol) injeta contexto rico de código/ferramentas na IA
com enorme economia de tokens. Esta seção é um **catálogo genérico** + o padrão
de como wirear qualquer servidor.

## Por que usar
- Contexto de código sem ler arquivo por arquivo (economia de tokens).
- Ferramentas externas (DB, CRM, scrapers, APIs) viram tools nativas da IA.
- Cross-sessão: memória de conversas antigas.

## Catálogo de servidores úteis (genéricos)
| Servidor | Função | Quando usar |
|---|---|---|
| **Graphify** (`graphify-scan`) | Knowledge Graph do código via AST. ~160x mais eficiente que grep. | Dead code, dependências circulares, lógica duplicada. |
| **Codebase Memory MCP** | Memória para repositórios grandes. ~120x menos tokens que grep. | Repos grandes, navegação rápida. |
| **Claude Mem** | Memória transversal contínua (cross-sessão). | Resgatar contexto de sessões antigas. |
| **Custom MCP (seu)** | Expor sua API/CRM/scraper como tools. | Qualquer sistema interno que a IA deva operar. |

## Padrão de como wirear um MCP (stdio)
1. O servidor é um script (Python/Node) que fala JSON-RPC sobre stdio.
2. Registrar no client da IA (ex.: `hermes mcp add` / config do Claude / OpenClaw).
3. Passar `command` (interpreter) + `args` (script) + `env` (secrets em runtime,
   **nunca hardcode** no config versionado).
4. **Sempre** reiniciar a IA após registrar (discovery acontece no startup).

## Pitfalls genéricos (válidos para qualquer MCP stdio)
1. **Version-check no handshake** — servidores que batem em pypi/npm no init podem
   travar o handshake stdio. Desligar com flag de banner/`--no-version-check`.
2. **Prompt interativo na inicialização** — libs que pedem `[y/N]` (ex.: tracing)
   travam o stdio. Desligar via env (`TRACING_ENABLED=false`, `DISABLE_TELEMETRY=true`).
3. **Import preguiçoso lento** — se o servidor demora ~10s p/ importar libs pesadas,
   importar no topo para não estourar timeout da 1ª chamada.
4. **DNS intermitente no venv** — `run` pode dar 'Connection error' esporádico;
   re-tentar com backoff.
5. **Config protegido** — se o client proíbe edição direta do config (ex.: `config.yaml`),
   usar SEMPRE a CLI oficial (`mcp add`) — nunca patch manual.
6. **Rede localhost IPv6** — `localhost` pode resolver `::1` e travar; usar
   `127.0.0.1` explícito nos endpoints.

> Para documentar um MCP específico que você criar, use `mcp-server-template.md`.
