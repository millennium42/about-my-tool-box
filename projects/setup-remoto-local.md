# Como Iniciar QUALQUER Projeto (remoto do git ou local)

Checklist de partida que eu uso. O objetivo: zerar contexto e ter ambiente rodando
sem re-explicar nada — este repo É o contexto.

---

## A. Projeto remoto (git clone)
```bash
# 1. Clonar
git clone <repo-url> && cd <repo>

# 2. Ler a spec/cabeçalho do projeto (se houver)
cat specs/*.md README.md 2>/dev/null

# 3. Subir dependências via Docker (padrão da minha stack)
docker compose up -d          # PostgreSQL, Redis, Maps Scraper, Crawl4AI

cd relaticle && docker compose up -d
# Acesso: http://localhost:8000 | admin sysadmin@relaticle.com / password123

# 5. Conectar ferramentas de IA ao projeto
#    - Hermes lê AGENTS.md / CLAUDE.md / .cursorrules do workdir
#    - MCP servers já registrados globalmente (crewai, relaticle)
```

## B. Projeto local (novo)
```bash
# 1. Estrutura modular canônica
mkdir -p specs scripts docker && touch README.md

# 2. Definir spec primeiro (Ralph Loop /spec)
#    → specs/nome-feature.md (objetivo, requisitos, restrições, "concluído")

# 3. Stack por tipo de projeto:
#    - Automação       → Python 3.11 (venv Hermes) + Docker
#    - Multiagente     → CrewAI MCP (Hermes como LLM, sem chave externa)
```

## C. Conectar minha stack de IA (sempre)
- **Hermes Agent** já tem skills + MCPs globais (crewai, relaticle, simplify-code...).
- **CrewAI**: `mcp_crewai_run_crew` / `spawn_research_crew` / `crewai_health`.
  Reiniciar Hermes após registrar novo MCP (`hermes mcp add`).
- **OpenClaw** (opcional): `openclaw dashboard --no-open` → URL com token.
- **Google Maps Scraper**: `POST :8081/api/v1/jobs` → polling → `GET :8081/api/v1/jobs/{id}/download` (CSV).
- **Crawl4AI**: `POST 127.0.0.1:11235/crawl` com `urls` (lista). Auth `Bearer hermes_crawl_super_secret_2026`.

## D. Regras ao iniciar (não esquecer)
1. Nunca inventar dados de teste — usar leads/dados reais ou claramente marcados.
2. LGPD: zero PII em logs; opt-out obrigatório em prospecção.
3. Commits granulares + documentação viva (atualizar README/skills junto).
4. `continue` retoma trabalho sem re-explicar contexto.

## E. Troubleshooting rápido
- **RedisException getaddrinfo**: Redis ext do PHP ausente (`pecl install redis`) ou
  `APP_KEY` hardcoded no compose sobrescrevendo .env.
- **Crawl4AI IPv6 trap**: usar `127.0.0.1:11235` (não `localhost` → `::1`).
- **Maps Scraper 404 no download**: query genérica demais — usar categoria específica
  (restaurante, pet shop), não "empresa santa maria".
- **CrewAI 'Connection error'**: DNS intermitente do venv — re-tentar.
