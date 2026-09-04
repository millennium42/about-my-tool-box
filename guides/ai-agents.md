# Adaptação entre agentes de IA

O fluxo é independente do cliente. Recursos disponíveis, arquivos de instrução e
modelo de cobrança mudam; o contrato de spec, privacidade e evidência não muda.

| Cliente | Fonte oficial | Modelo | Arquivo/contexto comum | Alternativa OSS inicial | O que confirmar |
|---|---|---|---|---|---|
| Codex | [produto](https://openai.com/codex/) | Pago/híbrido | `AGENTS.md`, skills e ferramentas conectadas | [OpenHands](https://github.com/OpenHands/OpenHands) | sandbox, permissões, modelo, custo e integrações reais |
| Claude Code | [documentação](https://docs.anthropic.com/en/docs/claude-code) | Pago/híbrido | `CLAUDE.md`, skills e MCP | [Aider](https://github.com/Aider-AI/aider) | escopo de comandos, memória, MCP e plano aplicável |
| Cursor | [documentação](https://cursor.com/docs) | Freemium/híbrido | regras do projeto e contexto indexado | [Cline](https://github.com/cline/cline) | arquivos incluídos, privacidade, modelo e modo agente |
| Outro agente | fonte exata a identificar | Desconhecido | instruções fornecidas explicitamente | pesquisar pelo requisito | acesso a arquivos, rede, comandos e persistência |

Use [o prompt inicial do README](../README.md) e mantenha no projeto uma fonte
canônica de spec e decisões. Não assuma que MCP, plugin, skill ou CLI está instalado
porque aparece neste catálogo.

Se o cliente ou provedor tiver plano pago, compare com
[alternativas open source](../catalog/paid-services.md). A alternativa precisa ser
avaliada pelo requisito: um agente self-hosted pode exigir modelo, sandbox,
observabilidade e operação que o serviço comercial já fornece.

Ao trocar de agente, repita pelo menos: leitura das instruções, caso mínimo, teste de
negação de permissão, privacidade, custo e formato do handoff.
