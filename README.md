# About My Tool Box — Base de Conhecimento

Repositório **genérico e reutilizável** usado como base de conhecimento pela IA
ao iniciar **QUALQUER projeto novo (virgem)** — remoto (git) ou local.

> Não é um registro de projetos específicos: é um conjunto de princípios,
> metodologias, catálogos de stack e templates que valem para qualquer projeto.
> Toda ferramenta citada aponta para o repositório oficial no GitHub.

## Como usar este repo (ordem de leitura)
1. `philosophies/` → princípios universais que DEVO seguir.
2. `methodologies/` → como executo (Ralph Loop, kickoff de projeto, Humanizer).
3. `mcp_servers/` → o que conecto à IA para contexto de código + como wirear MCP.
4. `plugins/` → catálogo de stack por camada (opções, não imposição).
5. `projects/` → TEMPLATES para documentar o novo projeto (spec + checklist).

## Perfil de Trabalho (como eu opero — reutilizável)
- **Comunicação**: direta, pragmática, técnica, SEM enrolação.
- **Idioma**: português.
- **Execução**: prefiro executar até o fim sem confirmar a cada passo
  (exceto ações destrutivas). Comando `continue` retoma sem re-explicar.
- **Entrega**: artefato funcionando com output real de execução — não stub.

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
│   ├── ralph_loop.md              # Workflow padrão (spec→build→review→learn)
│   ├── project-kickoff.md         # Kickoff genérico de projeto novo
│   └── humanizer.md               # Tom humano em comunicação automatizada
├── mcp_servers/
│   ├── mcp_catalog.md            # Catálogo de MCPs úteis + como wirear
│   └── mcp-server-template.md    # Template p/ documentar um MCP
├── plugins/
│   └── stack-catalog.md          # Catálogo de stack por camada (opções)
└── projects/
    ├── spec-template.md           # Template de spec de feature/projeto
    └── setup-checklist.md         # Checklist genérico de início
```

## Ecossistema de ferramentas referenciado (repos oficiais)
| Ferramenta | Repositório oficial | Função |
|---|---|---|
| Ponytail (YAGNI) | https://github.com/DietrichGebert/ponytail | Agente age como "dev sênior preguiçoso"; não escreve código desnecessário |
| m1nd / rtk / probe | https://github.com/DietrichGebert (toolset) | Orientação estrutural; wrapper de shell; revisão de PR |
| Graphify | https://github.com/Graphify-Labs/graphify | Knowledge graph do código via AST (economia de tokens) |
| Ralph Loop | https://github.com/snarktank/ralph | Loop autônomo de agente AI (spec→build→review→learn) |
| Humanizer | https://github.com/blader/humanizer | Remove sinais de texto gerado por IA |
| Superpowers | https://github.com/obra/superpowers | Framework de skills + método de dev de software |
| Ruflo | https://github.com/ruvnet/ruflo | Meta-harness, swarms, memória HNSW |
| CrewAI | https://github.com/crewAIInc/crewAI | Orquestração multiagente role-playing |
| Crawl4AI | https://github.com/unclecode/crawl4ai | Web crawler LLM-friendly, open-source |
| Google Maps Scraper | https://github.com/gosom/google-maps-scraper | Scraper local de Google Maps (alt. open ao Apify) |
| MCP | https://github.com/modelcontextprotocol/modelcontextprotocol | Especificação e docs do Model Context Protocol |
| Filament | https://github.com/filamentphp/filament | Framework UI open-source para Laravel |
| Livewire | https://github.com/livewire/livewire | Full-stack framework para Laravel |
| Twenty | https://github.com/twentyhq/twenty | Alternativa open ao Salesforce, feita para IA |
