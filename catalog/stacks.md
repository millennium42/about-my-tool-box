# Perfis de stack

Estas são opções iniciais, não receitas obrigatórias. Comece pelo menor perfil que
atende à spec e registre toda exceção.

| Tipo de projeto | Kit mínimo sugerido | Adições somente se necessário |
|---|---|---|
| Web full-stack | Node.js/TypeScript ou Laravel + PostgreSQL | Redis, Sentry, UI kit |
| Automação | Python | Docker, fila, observabilidade |
| IA/multiagente | Python ou TypeScript + SDK do provedor | CrewAI, LangGraph, MCP |
| Scraping | Python + Playwright | Crawl4AI, Firecrawl, armazenamento |
| Dados/ETL | Python + PostgreSQL | orquestrador, cache, jobs |
| Landing page | HTML/CSS/JS ou Next.js | UI kit, animação |
| CRM/admin | Laravel + Filament/Livewire | Redis, filas, auditoria |

Git, Python, Node.js, Docker e Docker Compose estão no kit verificado. As demais
opções precisam ser validadas antes de entrar como dependência padrão.
