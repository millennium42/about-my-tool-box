# Kickoff de Projeto Novo (genérico)

Como iniciar um projeto virgem usando esta base de conhecimento.
Aplica-se a projeto remoto (git clone) ou local (do zero).

## Passo 1 — Contexto
- Identificar: objetivo de negócio, usuário final, restrições (jurídicas, de stack, de prazo).
- Escolher onde a IA vai operar: workdir local ou clone remoto.

## Passo 2 — Spec (Ralph Loop /spec)
- Criar `specs/nome-feature.md` a partir de `projects/spec-template.md`.
- Definir: objetivo, requisitos indispensáveis, restrições, definição de "concluído".
- **Não construir ainda.**

## Passo 3 — Seleção de Stack
Usar `plugins/stack-catalog.md` como catálogo de opções. Decidir por camada:
- Frontend / Backend / Banco / Infra / LLM·Agentes / Scraping / Observabilidade.
- Critério: menor atrito para o objetivo, não "o que está na moda".
- Aplicar **Ponytail**: preferir stdlib/plataforma nativa a nova dependência.

## Passo 4 — Scaffold
- Estrutura modular canônica: `specs/ scripts/ docker/ docs/`.
- Subir dependências (Docker Compose para DB/cache/serviços auxiliares).
- Conectar ferramentas de IA ao workdir (ler `AGENTS.md`/`CLAUDE.md`/`.cursorrules`).
- Se o repo for grande: construir o Graphify cedo (`graphify extract . --out .`).

## Passo 5 — Build & Verify (Ralph Loop /build → /review)
- Construir EXATAMENTE a spec.
- Verificar com execução real (testes, healthcheck, status code) — não por fé.
- Documentar vivo.

## Passo 6 — Documentar o projeto
- Preencher `projects/spec-template.md` (segunda metade) com o estado real do projeto
  recém-criado (stack, status, regras de negócio, decisões). Isso vira o "cérebro"
  do projeto para sessões futuras.

## Árvore de decisão rápida (stack)
| Se o projeto é... | Stack sugerida (opções no catalog) |
|---|---|
| Web app pesado / CRM | Framework backend MVC (Laravel/Filament) + PostgreSQL + Redis |
| Automação / scripts | Python + Docker |
| Multiagente / IA | Orquestrador (CrewAI/LangGraph) + LLM via MCP |
| Landing / marketing | Next.js + TypeScript + UI kit |
| Dados / ETL | Python + Postgres + orquestrador de jobs |

## Referências git para kickoff
- Ralph Loop: https://github.com/snarktank/ralph
- Ponytail: https://github.com/DietrichGebert/ponytail
- Superpowers: https://github.com/obra/superpowers
- Graphify: https://github.com/Graphify-Labs/graphify
