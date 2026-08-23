# Catálogo de Stack (por camada)

Catálogo de **opções** de tecnologia por camada. Não é imposição — é o ponto
de partida para selecionar stack num projeto novo. Critério: menor atrito
para o objetivo, não "o que está na moda". Aplicar Ponytail: preferir
stdlib/plataforma nativa a nova dependência.

## Frontend
- **Framework**: Next.js + React (padrão web), ou framework do backend (Livewire/Blazor).
  - Livewire: https://github.com/livewire/livewire (⭐ 23k+)
- **Linguagem**: TypeScript (strict) onde houver tipo complexo.
- **UI**: shadcn/ui, MagicUI, ReactBits, 21st.dev (componentes prontos).
- **Animações** (só se estritamente necessário): Three.js, GSAP, Anime.js, Framer Motion.

## Backend
- **Linguagem**: Python (automação/scripts), TypeScript/Node (stack integrada),
  PHP/Laravel (CRM web pesado).
  - Filament (UI Laravel): https://github.com/filamentphp/filament (⭐ 31k+)
  - Livewire: https://github.com/livewire/livewire
- **Banco relacional default**: PostgreSQL.
- **Auth**: BetterAuth / Auth provider do framework.
- **Cache/Filas**: Redis (Upstash para serverless).
- **Observabilidade**: Sentry.

## Infra / Containers
- **Containers**: Docker + Docker Compose (stack completa: DB, cache, serviços aux.).
- **Orquestração**: Kubernetes se necessário.
- **Deploy**: Render / AWS / Vercel; self-hosted: Coolify.
- **SaaS de suporte**: Supabase (banco/auth/storage acelerado).

## LLM / Agentes
- **LLM**: provider OpenAI-compatível (Nous, OpenAI, etc).
- **Orquestração multiagente**:
  - CrewAI: https://github.com/crewAIInc/crewAI (⭐ 57k+) — role-playing agents.
  - LangGraph, AutoGen (alternativas).
- **Operator/Gateway**: OpenClaw (expõe IA como operator com MCPs conectados).
- **Loops de agente**:
  - Ralph: https://github.com/snarktank/ralph (⭐ 21k+)
  - Superpowers: https://github.com/obra/superpowers (⭐ 276k+)
  - Ruflo: https://github.com/ruvnet/ruflo (⭐ 68k+)

## Browsing / Web Scraping
- **Orquestração de navegador**: Browser Use, Playwright, Chrome MCP.
- **Extração de dados**:
  - Crawl4AI: https://github.com/unclecode/crawl4ai (⭐ 79k+) — LLM-friendly crawler.
  - Firecrawl, Dify, Maxun.
- **Alternativa open-source a Apify**: Google Maps Scraper local
  (https://github.com/gosom/google-maps-scraper — ⭐ 5.5k+).

## Marketing / Growth
- **Humanizer** (https://github.com/blader/humanizer — ⭐ 37k+): tom humano em copy/mensagens.
- **Corey Haines 31 / MarketingSkills**: CRO, SEO, Copywriting.

## Orquestração Avançada
- OpenHands, LangFlow, Perplexity MCP, Ruflo (swarms).

## Qualidade & Segurança (plugins ativos por padrão)
- **Security Essentials & OWASP Guard**: bloqueiam commit com PII, validam senhas
  expostas, blindam SQL Injection / XSS / CSRF.
- **Code Review**: code-review, Context7, Matt Pocock, Hamel Husain evals.
- **probe** (https://github.com/getprobe-dev/probe-extension): revisão de código
  por IA em PRs do GitHub.
- **Verificação de secrets** antes de cada commit (zero credencial no diff).

## Exemplo de compose canônico (DB + cache + scraper)
```yaml
services:
  postgres:
    image: postgres:16
    environment: { POSTGRES_USER: app, POSTGRES_PASSWORD: app, POSTGRES_DB: app }
    ports: ["5432:5432"]
  redis:
    image: redis:7
    ports: ["6379:6379"]
  maps-scraper:
    image: gosom/google-maps-scraper
    ports: ["8081:8080"]
```
