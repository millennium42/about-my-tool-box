# Template — Documentar um MCP Server

Copie este arquivo para `mcp_servers/<nome>.md` sempre que criar/wirear um MCP.
Mantenha genérico e reutilizável (sem segredos, sem paths de máquina específica).

```markdown
# <Nome do MCP>

**Status**: (ativo / em espera / verificado e2e)
**Repositório oficial**: https://github.com/<org>/<repo>

## O que faz
- Resumo de 1–2 linhas do que o servidor expõe.

## Ferramentas expostas
- `tool_1`: descrição. Args: (listar).
- `tool_2`: descrição. Args: (listar).

## Como a autenticação funciona (runtime, sem hardcode)
- Lê secrets de <env var> / <auth file> em runtime.
- Aponta para <serviço> com <base_url> + <api_key de env>.

## Pré-requisitos
- Python/Node versão.
- Pacotes necessários (ex.: fastmcp, crewai).

## Como usar
1. Reiniciar a IA (discovery no startup).
2. Pedir normalmente: "<exemplo de prompt que dispara a tool>".

## Pitfalls resolvidos (não repetir)
1. ...
2. ...

## Comandos
\`\`\`bash
# registrar (CLI oficial, nunca patch no config)
<mcp add ...>
# testar
<mcp test ...>
\`\`\`

## Verificação (evidência de que funciona)
- <status de teste>
- <execução real comprovada>
```

---

## Exemplo de preenchimento (CrewAI MCP)
```markdown
# CrewAI MCP
**Status**: verificado e2e
**Repositório oficial**: https://github.com/crewAIInc/crewAI

## O que faz
Expõe orquestração multiagente CrewAI como tools nativas da IA, usando um
LLM OpenAI-compatível como backend de inferência (sem chave de provedor externa).

## Ferramentas expostas
- `run_crew`: executa crew declarativa. Args: task, agents, process, temperature, timeout.
- `spawn_research_crew`: crew pronta de 3 agentes. Args: topic, depth (quick|standard).
- `crewai_health`: status, modelo, auth (sem expor chave).

## Como a autenticação funciona
Lê em runtime HERMES_HOME/auth.json → agent_key + inference_base_url.
Aponta LLM(base_url=..., api_key=agent_key). Modelo padrão via env HERMES_CREW_MODEL.

## Pitfalls resolvidos
1. mcp.run(transport="stdio", show_banner=False) — evita version-check no pypi.
2. CREWAI_TRACING_ENABLED=false — evita prompt [y/N] que trava stdio.
3. DNS intermitente → re-tentar com backoff.
```
