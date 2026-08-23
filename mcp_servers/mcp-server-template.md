# Template — Documentar um MCP Server

Copie este arquivo para `mcp_servers/<nome>.md` sempre que criar/wirear um MCP.
Mantenha genérico e reutilizável (sem segredos, sem paths de máquina específica).

```markdown
# <Nome do MCP>

**Status**: (ativo / em espera / verificado e2e)

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
- Pacotes necessários.

## Como usar
1. Reiniciar a IA (discovery no startup).
2. Pedir normalmente: "<exemplo de prompt que dispara a tool>".

## Pitfalls resolvidos (não repetir)
1. ...
2. ...

## Comandos
\`\`\`bash
# registrar
<mcp add ...>
# testar
<mcp test ...>
\`\`\`

## Verificação (evidência de que funciona)
- <status de teste>
- <execução real comprovada>
```
