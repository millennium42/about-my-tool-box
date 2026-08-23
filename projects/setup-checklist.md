# Checklist de Início de Projeto (genérico)

Usado para iniciar QUALQUER projeto — remoto (git) ou local. O objetivo é zerar
contexto e ter ambiente rodando sem re-explicar nada (este repo É o contexto).

## A. Projeto remoto (git clone)
```bash
# 1. Clonar
git clone <repo-url> && cd <repo>

# 2. Ler cabeçalho do projeto
cat specs/*.md README.md 2>/dev/null

# 3. Subir dependências (padrão: Docker Compose)
docker compose up -d          # DB, cache, serviços auxiliares

# 4. Backend web pesado (ex.: Laravel/Filament-style)
cd <app> && docker compose up -d
# Acesso: http://localhost:<porta>

# 5. Conectar ferramentas de IA ao projeto
#    - IA lê AGENTS.md / CLAUDE.md / .cursorrules do workdir
#    - MCPs registrados globalmente já ficam disponíveis
```

## B. Projeto local (novo / virgem)
```bash
# 1. Estrutura modular canônica
mkdir -p specs scripts docker docs && touch README.md

# 2. Definir spec primeiro (Ralph Loop /spec)
#    → specs/<nome>.md (objetivo, requisitos, restrições, "concluído")

# 3. Selecionar stack (ver plugins/stack-catalog.md)
#    - Web pesado   → framework backend MVC + PostgreSQL + Redis
#    - Automação    → Python + Docker
#    - Multiagente  → orquestrador + LLM via MCP
```

## C. Conectar stack de IA (sempre que aplicável)
- **IA Agent** já tem skills + MCPs globais.
- **MCP custom**: registrar via CLI oficial (`mcp add`), nunca patch no config.
- **Operator/Gateway** (ex.: OpenClaw): dashboard com URL autenticada (token em query).
- **Scraper/Enriquecedor**: subir container, usar `127.0.0.1` explícito (não `localhost`).

## D. Regras ao iniciar (não esquecer)
1. Nunca inventar dados de teste — usar dados reais ou claramente marcados.
2. Compliance: zero PII em logs; opt-out obrigatório em outreach.
3. Commits granulares + documentação viva (atualizar README/skills junto).
4. `continue` retoma trabalho sem re-explicar contexto.

## E. Troubleshooting padrão
- **DB connection falha (getaddrinfo)**: extensão do driver ausente OU `APP_KEY`/
  secrets hardcoded sobrescrevendo env. Usar secrets em runtime.
- **Endpoint travando em IPv6**: usar `127.0.0.1` em vez de `localhost`.
- **Scraper 404 no download**: query genérica demais — usar categoria específica.
- **Run remoto 'Connection error'**: DNS intermitente — re-tentar com backoff.
- **MCP não aparece**: reiniciar a IA (discovery é no startup).
