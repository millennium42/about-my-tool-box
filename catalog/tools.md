# Catálogo completo de ferramentas

Esta tabela preserva as ferramentas já citadas na base e organiza as opções
adicionadas pelos playbooks. O status é deliberado: no momento, somente o kit de
ferramentas de base foi executado nesta revisão. Ferramentas externas permanecem
em avaliação até que a instalação, o uso mínimo e a verificação sejam repetidos.

| Ferramenta | Tipo | Para que serve | Status | Fonte oficial |
|---|---|---|---|---|
| Git | CLI | Versionamento e colaboração | Verificada | [git-scm.com](https://git-scm.com/) |
| Python | Runtime | Automação, scripts e dados | Verificada | [python.org](https://www.python.org/) |
| Node.js | Runtime | JavaScript, TypeScript e ferramentas web | Verificada | [nodejs.org](https://nodejs.org/) |
| npm | Gerenciador | Dependências e scripts Node | Verificada | [npmjs.com](https://www.npmjs.com/) |
| Docker | Containers | Ambientes isolados e reproduzíveis | Verificada | [docker.com](https://www.docker.com/) |
| Docker Compose | Orquestração local | Subir vários serviços localmente | Verificada | [docs.docker.com/compose](https://docs.docker.com/compose/) |
| GitHub Actions | CI/CD | Automatizar validação e entrega | Em avaliação | [docs.github.com/actions](https://docs.github.com/en/actions) |
| Codex | Agente de IA | Construir, revisar e operar projetos | Referência | [openai.com/codex](https://openai.com/codex/) |
| Ponytail | Princípio | Aplicar YAGNI e reduzir dependências | Referência | [GitHub](https://github.com/DietrichGebert/ponytail) |
| m1nd | CLI/orientação | Orientar exploração estrutural | Em avaliação | [autor no GitHub](https://github.com/DietrichGebert) |
| rtk | Wrapper CLI | Reduzir saída de shell e navegar código | Em avaliação | [autor no GitHub](https://github.com/DietrichGebert) |
| probe | Code review | Revisar código por IA em PRs | Em avaliação | [probe-extension](https://github.com/getprobe-dev/probe-extension) |
| Graphify | CLI/análise | Criar grafo AST do código | Em avaliação | [Graphify](https://github.com/Graphify-Labs/graphify) |
| Ralph Loop | Metodologia | Organizar spec, build, review e aprendizado | Referência | [Ralph](https://github.com/snarktank/ralph) |
| Humanizer | Skill/metodologia | Tornar texto automatizado mais natural | Em avaliação | [Humanizer](https://github.com/blader/humanizer) |
| Superpowers | Skills/metodologia | Brainstorm, TDD, subagentes e review | Em avaliação | [Superpowers](https://github.com/obra/superpowers) |
| Ruflo | Meta-harness | Orquestrar swarms e memória | Em avaliação | [Ruflo](https://github.com/ruvnet/ruflo) |
| CrewAI | Framework multiagente | Orquestrar agentes, tarefas e crews | Em avaliação | [CrewAI](https://github.com/crewAIInc/crewAI) |
| LangGraph | Framework multiagente | Modelar fluxos de agentes como grafos | Em avaliação | [LangGraph](https://github.com/langchain-ai/langgraph) |
| AutoGen | Framework multiagente | Construir conversas e agentes colaborativos | Em avaliação | [AutoGen](https://github.com/microsoft/autogen) |
| OpenHands | Agente de código | Executar tarefas de desenvolvimento com IA | Em avaliação | [OpenHands](https://github.com/All-Hands-AI/OpenHands) |
| OpenClaw | Gateway/operator | Expor IA e integrações como operador | Em avaliação | — |
| FastMCP | SDK MCP | Criar servidores MCP em Python | Em avaliação | [FastMCP](https://github.com/jlowin/fastmcp) |
| MCP | Protocolo | Conectar modelos, contexto e ferramentas | Referência | [MCP](https://github.com/modelcontextprotocol/modelcontextprotocol) |
| Filesystem MCP | Servidor MCP | Expor arquivos com escopo controlado | Em avaliação | [servidores MCP](https://github.com/modelcontextprotocol/servers) |
| Fetch MCP | Servidor MCP | Buscar conteúdo HTTP para a IA | Em avaliação | [servidores MCP](https://github.com/modelcontextprotocol/servers) |
| PostgreSQL MCP | Servidor MCP | Consultar banco via IA | Em avaliação | [servidores MCP](https://github.com/modelcontextprotocol/servers) |
| Codebase Memory MCP | Memória/MCP | Recuperar contexto de repositórios grandes | Em avaliação | — |
| Claude Mem | Memória | Recuperar contexto entre sessões | Em avaliação | — |
| Custom MCP | Integração | Expor API, CRM ou scraper próprio | Em avaliação | [SDK MCP](https://github.com/modelcontextprotocol) |
| Next.js | Framework web | Aplicações React full-stack | Em avaliação | [Next.js](https://github.com/vercel/next.js) |
| React | Biblioteca web | Construir interfaces | Em avaliação | [React](https://github.com/facebook/react) |
| TypeScript | Linguagem | Tipagem estática para JavaScript | Em avaliação | [TypeScript](https://github.com/microsoft/TypeScript) |
| Laravel | Framework web | Aplicações PHP MVC | Em avaliação | [Laravel](https://github.com/laravel/laravel) |
| Filament | UI Laravel | Painéis e backoffice | Em avaliação | [Filament](https://github.com/filamentphp/filament) |
| Livewire | UI Laravel | Interfaces reativas com PHP | Em avaliação | [Livewire](https://github.com/livewire/livewire) |
| Better Auth | Autenticação | Autenticação para aplicações TypeScript | Em avaliação | [Better Auth](https://github.com/better-auth/better-auth) |
| PostgreSQL | Banco | Banco relacional | Em avaliação | [postgresql.org](https://www.postgresql.org/) |
| Redis | Cache/filas | Cache, sessão e filas | Em avaliação | [Redis](https://github.com/redis/redis) |
| Upstash | SaaS | Redis serverless e serviços de dados | Em avaliação | [upstash.com](https://upstash.com/) |
| Sentry | Observabilidade | Erros, performance e alertas | Em avaliação | [Sentry](https://sentry.io/) |
| Kubernetes | Orquestração | Operar containers em escala | Referência | [kubernetes.io](https://kubernetes.io/) |
| Render | Deploy | Hospedar serviços e bancos | Em avaliação | [render.com](https://render.com/) |
| AWS | Cloud | Infraestrutura e serviços gerenciados | Referência | [aws.amazon.com](https://aws.amazon.com/) |
| Vercel | Deploy | Frontend e funções serverless | Em avaliação | [vercel.com](https://vercel.com/) |
| Coolify | PaaS self-hosted | Hospedar aplicações próprias | Em avaliação | [Coolify](https://github.com/coollabsio/coolify) |
| Supabase | Backend SaaS | Banco, auth, storage e APIs | Em avaliação | [Supabase](https://github.com/supabase/supabase) |
| OpenAI API | LLM/API | Modelos e ferramentas de IA | Em avaliação | [Platform docs](https://platform.openai.com/docs/overview) |
| Nous Research | LLM/provedor | Modelos e inferência compatível | Em avaliação | [Nous Research](https://nousresearch.com/) |
| Browser Use | Automação web | Controlar navegador com agente | Em avaliação | [Browser Use](https://github.com/browser-use/browser-use) |
| Playwright | Automação web | Testar e controlar navegadores | Em avaliação | [Playwright](https://github.com/microsoft/playwright) |
| Chrome DevTools MCP | MCP/browser | Inspecionar e controlar Chrome | Em avaliação | [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| Crawl4AI | Scraping | Crawler orientado a LLM | Em avaliação | [Crawl4AI](https://github.com/unclecode/crawl4ai) |
| Firecrawl | Scraping SaaS | Crawling e extração via API | Em avaliação | [Firecrawl](https://github.com/mendableai/firecrawl) |
| Dify | Plataforma IA | Criar aplicações e workflows de IA | Em avaliação | [Dify](https://github.com/langgenius/dify) |
| Maxun | Scraping | Extração visual/no-code | Em avaliação | [Maxun](https://github.com/getmaxun/maxun) |
| Google Maps Scraper | Scraping | Coletar dados autorizados de mapas | Em avaliação | [google-maps-scraper](https://github.com/gosom/google-maps-scraper) |
| Apify | Scraping SaaS | Atores, crawling e automação | Referência | [apify.com](https://apify.com/) |
| Three.js | Web 3D | Gráficos tridimensionais | Referência | [Three.js](https://github.com/mrdoob/three.js) |
| GSAP | Animação | Animações avançadas na web | Referência | [gsap.com](https://gsap.com/) |
| Anime.js | Animação | Animações leves | Referência | [Anime.js](https://github.com/juliangarnier/anime) |
| Motion | Animação React | Animações e gestos em interfaces | Referência | [Motion](https://github.com/motiondivision/motion) |
| shadcn/ui | UI | Componentes copiáveis para React | Em avaliação | [shadcn/ui](https://github.com/shadcn-ui/ui) |
| Magic UI | UI | Componentes visuais para React | Em avaliação | [Magic UI](https://github.com/magicuidesign/magicui) |
| React Bits | UI | Componentes visuais prontos | Em avaliação | [React Bits](https://github.com/DavidHDev/react-bits) |
| 21st.dev | UI/geração | Componentes e interfaces assistidos por IA | Em avaliação | [21st.dev](https://21st.dev/) |
| Corey Haines MarketingSkills | Marketing | CRO, SEO e copywriting | Em avaliação | — |
| OpenAI Evals | Avaliação IA | Avaliar saídas e comportamentos de modelos | Em avaliação | [OpenAI Evals](https://github.com/openai/evals) |
| Context7 | Documentação/MCP | Consultar documentação atualizada | Em avaliação | [Context7](https://github.com/upstash/context7) |
| Security Essentials | Segurança | Verificações de segurança de projeto | Referência | — |
| OWASP Guard | Segurança | Verificações baseadas em OWASP | Referência | [OWASP](https://owasp.org/) |
| Code review | Prática | Revisão contra requisito e risco | Referência | — |
| Matt Pocock / Total TypeScript | Educação | Boas práticas e avaliação de TypeScript | Referência | [Total TypeScript](https://www.totaltypescript.com/) |
| Twenty | CRM open source | CRM extensível e orientado a IA | Em avaliação | [Twenty](https://github.com/twentyhq/twenty) |
| Ferramenta arquivada | Histórico | Entrada removida ou sem manutenção suficiente | Arquivada | — |

## Como o status muda

Uma entrada só pode passar para **Verificada** quando preencher o modelo de
[tool-entry-template.md](tool-entry-template.md) com evidência E3. Para serviços
pagos, registre também custo, região, retenção de dados e alternativa disponível.
