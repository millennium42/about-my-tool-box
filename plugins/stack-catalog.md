# Catálogo de Stack (por camada)

Catálogo de **opções** de tecnologia por camada. Não é imposição — é o ponto
de partida para selecionar stack num projeto novo. Critério: menor atrito
para o objetivo, não "o que está na moda".

## Frontend
- **Framework**: Next.js + React (padrão web), ou framework do backend (Livewire/Blazor).
- **Linguagem**: TypeScript (strict) onde houver tipo complexo.
- **UI**: shadcn/ui, MagicUI, ReactBits, 21st.dev (componentes prontos).
- **Animações** (só se estritamente necessário): Three.js, GSAP, Anime.js, Framer Motion.

## Backend
- **Linguagem**: Python (automação/scripts), ou TypeScript/Node (stack integrada),
  ou PHP/Laravel (CRM web pesado).
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
- **Orquestração multiagente**: CrewAI, LangGraph, AutoGen.
- **Operator/Gateway**: OpenClaw ((expõe IA como operator com MCPs conectados)).

## Browsing / Web Scraping
- **Orquestração de navegador**: Browser Use, Playwright, Chrome MCP.
- **Extração de dados**: Crawl4AI, Firecrawl, Dify, Maxun.
- **Alternativa open-source a Apify**: Google Maps Scraper local (gosom).

## Marketing / Growth
- **Humanizer** (`github.com/blader/humanizer`): tom humano em copy/mensagens.
- **Corey Haines 31 / MarketingSkills**: CRO, SEO, Copywriting.

## Orquestração Avançada
- OpenHands, LangFlow, Perplexity MCP, Ruflo (swarms).

## Qualidade & Segurança (plugins ativos por padrão)
- **Security Essentials & OWASP Guard**: bloqueiam commit com PII, validam senhas
  expostas, blindam SQL Injection / XSS / CSRF.
- **Code Review**: code-review, Context7, Matt Pocock, Hamel Husain evals.
- **Verificação de secrets** antes de cada commit (zero credencial no diff).
