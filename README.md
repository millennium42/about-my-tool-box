# About My Tool Box — Base de Conhecimento

Repositório **genérico e reutilizável** usado como base de conhecimento pela IA
ao iniciar **QUALQUER projeto novo (virgem)** — remoto (git) ou local.

> Não é um registro de projetos específicos: é um conjunto de princípios,
> metodologias, catálogos de stack e templates que valem para qualquer projeto.

## Como usar este repo (ordem de leitura)
1. `philosophies/` → princípios universais que DEVO seguir (YAGNI, qualidade,
   compliance, finishing-the-job, verificação honesta).
2. `methodologies/` → como executo (Ralph Loop, kickoff de projeto).
3. `mcp_servers/` → o que conecto à IA para contexto de código + como wirear MCP.
4. `plugins/` → catálogo de stack por camada (opções, não imposição).
5. `projects/` → TEMPLATES para documentar o novo projeto (spec + checklist).

## Perfil de Trabalho (como eu opero — reutilizável)
- **Comunicação**: direta, pragmática, técnica, SEM enrolação.
- **Idioma**: português.
- **Execução**: prefiro executar até o fim sem confirmar a cada passo
  (exceto ações destrutivas). Comando `continue` retoma sem re-explicar.
- **Entrega**: artefato funcionando com output real de execução — não stub,
  não plano bonito.

## Regras de Ouro (não negociáveis, aplicáveis a qualquer projeto)
1. **Sem enrolação** — resultado real, não descrição de resultado.
2. **Finishing the job** — entrego artefato funcionando com output de execução real.
3. **Nunca inventar dados** — dados de teste só reais ou claramente marcados.
4. **Compliance** — zero PII em logs; sem mock em produção; migrations aplicadas
   não se editam; commit nunca quebra produção.
5. **Modular desde o nascimento** — código pronto pra escalar, documentação viva.
6. **Verificação honesta** — não afirmo que algo funciona sem evidência real.

## Estrutura
```
About-My-Tool-Box/
├── README.md                     # Este arquivo
├── philosophies/
│   └── working-principles.md     # Princípios universais de trabalho
├── methodologies/
│   ├── ralph_loop.md             # Workflow padrão (spec→build→review→learn)
│   └── project-kickoff.md        # Kickoff genérico de projeto novo
├── mcp_servers/
│   ├── mcp_catalog.md            # Catálogo de MCPs úteis + como wirear
│   └── mcp-server-template.md    # Template p/ documentar um MCP
├── plugins/
│   └── stack-catalog.md          # Catálogo de stack por camada (opções)
└── projects/
    ├── spec-template.md          # Template de spec de feature/projeto
    └── setup-checklist.md        # Checklist genérico de início
```
