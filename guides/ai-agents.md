# Adaptação entre agentes de IA

O conteúdo é centrado no Codex, mas os princípios são independentes do cliente.

| Cliente | Contexto inicial | Convenção equivalente |
|---|---|---|
| Codex | Informar o repositório e o perfil aplicável | `AGENTS.md`, skills, ferramentas conectadas |
| Claude Code | Informar o repositório e o perfil aplicável | `CLAUDE.md`, skills e MCP |
| Cursor | Informar o repositório e o perfil aplicável | `.cursor/rules` ou regras do projeto |
| Outro agente | Fornecer arquivos e comandos explicitamente | Arquivo de instruções suportado pelo cliente |

O agente deve distinguir o que está instalado no ambiente do que apenas está
descrito neste catálogo. Nunca assuma que um MCP, plugin ou skill está disponível
porque seu nome aparece em uma página.
