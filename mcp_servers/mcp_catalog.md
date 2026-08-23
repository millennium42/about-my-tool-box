# Catálogo de MCP Servers

MCP (Model Context Protocol) injeta contexto rico de código/ferramentas na IA
com enorme economia de tokens. Especificação oficial:
https://github.com/modelcontextprotocol/modelcontextprotocol (⭐ 9k+).

## Por que usar
- Contexto de código sem ler arquivo por arquivo (economia de tokens).
- Ferramentas externas (DB, CRM, scrapers, APIs) viram tools nativas da IA.
- Cross-sessão: memória de conversas antigas.

## Catálogo de servidores úteis (genéricos)
| Servidor | Repositório / Origem | Função | Quando usar |
|---|---|---|---|
| **Graphify** | https://github.com/Graphify-Labs/graphify | Knowledge Graph do código via AST. ~160x mais eficiente que grep. | Dead code, dependências circulares, lógica duplicada, mapa do projeto. |
| **Codebase Memory MCP** | (ecossistema MCP) | Memória para repositórios grandes. ~120x menos tokens que grep. | Repos grandes, navegação rápida. |
| **Claude Mem** | (skill cross-sessão) | Memória transversal contínua. | Resgatar contexto de sessões antigas. |
| **Custom MCP (seu)** | FastMCP / SDK oficial | Expor sua API/CRM/scraper como tools. | Qualquer sistema interno que a IA deva operar. |
| **Filesystem / Fetch / PostgreSQL** | https://github.com/modelcontextprotocol (servers oficiais) | Ler/escrever arquivos, buscar web, query em DB. | Uso geral. |

## Padrão de como wirear um MCP (stdio)
1. O servidor é um script (Python/Node) que fala JSON-RPC sobre stdio.
2. Registrar no client da IA (ex.: `hermes mcp add` / config do Claude / OpenClaw).
3. Passar `command` (interpreter) + `args` (script) + `env` (secrets em runtime,
   **nunca hardcode** no config versionado).
4. **Sempre** reiniciar a IA após registrar (discovery acontece no startup).

## Exemplo concreto (FastMCP + CrewAI como MCP)
Servidor expõe orquestração multiagente (https://github.com/crewAIInc/crewAI)
como tools nativas da IA, usando um LLM OpenAI-compatível como backend:
```python
# server.py (FastMCP)
from fastmcp import FastMCP
from crewai import Agent, Task, Crew, LLM
import os, json

mcp = FastMCP("meu-mcp")

@mcp.tool()
def run_crew(task: str, agents: list = None, process: str = "sequential") -> str:
    """Executa uma crew declarativa usando LLM OpenAI-compatível."""
    llm = LLM(
        model=f"openai/{os.environ.get('MY_MODEL','gpt-4o-mini')}",
        base_url=os.environ["MY_BASE_URL"],
        api_key=os.environ["MY_API_KEY"],   # secrets em runtime, nunca hardcoded
    )
    crew_agents = [Agent(role=a["role"], goal=a["goal"], backstory=a["backstory"], llm=llm)
                   for a in (agents or [{"role":"analyst","goal":"analyze","backstory":"senior"}])]
    crew = Crew(agents=crew_agents, tasks=[Task(description=task, agent=crew_agents[0])],
                process=process)
    return crew.kickoff().raw

if __name__ == "__main__":
    mcp.run(transport="stdio", show_banner=False)  # show_banner=False evita version-check no pypi
```
Registrar:
```bash
hermes mcp add meu-mcp \
  --command "python" --args "server.py" \
  --env MY_BASE_URL="https://..." --env MY_API_KEY="..." --env MY_MODEL="..."
```

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
