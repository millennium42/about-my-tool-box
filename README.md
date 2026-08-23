# About My Tool Box

Guia modular e **vivo** que consolida TUDO que eu conheço e uso de ferramentas,
metodologias, filosofias de trabalho, plugins e integrações MCP.

> Propósito: ser o ponto de partida para iniciar **QUALQUER** projeto — remoto (git)
> ou local — sem precisar reexplicar contexto. É o meu "cérebro externo" de setup.

## Quem Sou
- **Nome**: Millani (Pablo / Millani)
  - Email real: `codehouse42@gmail.com`
  - WhatsApp Business: `55 55 99144-1700` (pareado e ativo)
- **Nicho da agência**: Restaurantes / pequenos negócios em **Santa Maria / RS, Brasil**
- **Expertise**: Software Engineering, Data, AI, automação de prospecção B2B
- **Estilo de Comunicação**: DIRETO, pragmático, técnico, SEM enrolação.
  Respondo em português. Prefiro execução até o fim sem confirmar a cada passo.
- **Comando especial**: `continue` → retoma trabalho sem re-explicar.

## Como navegar este repo (modular)
Cada pasta é independente. Para iniciar um projeto novo, leia:
1. `philosophies/` → princípios que DEVO seguir (YAGNI, qualidade, LGPD, sem mock em prod).
2. `methodologies/` → como executo (Ralph Loop, Humanizer, prospecção).
3. `mcp_servers/` → o que conecto ao Hermes/Claude/OpenClaw para contexto de código.
4. `plugins/` → stack base + ferramentas de IA que uso no dia a dia.

## Stack canônica (o que eu uso de verdade)
- **Containers**: Docker Compose (PostgreSQL, Redis, Google Maps Scraper, Crawl4AI)
- **LLM**: Hermes Agent usando Nous (endpoint OpenAI-compat) — `tencent/hy3:free`
- **Multiagente**: CrewAI como MCP do Hermes (sem chave externa)
- **Operator/Gateway**: OpenClaw (Hermes como LLM)
- **Prospecção B2B**: Google Maps Scraper local → Crawl4AI → Hermes qualifica → WhatsApp

## Regras de ouro (não negociáveis)
1. **Sem enrolação** — entrego resultado real, não plano bonito.
2. **Finishing the job** — o entregável é artefato funcionando com output real de execução, não stub.
3. **Nunca inventar dados** — leads, depoimentos, números: só real. (LGPD: zero PII em logs.)
4. **Sem mock em produção** — migrations aplicadas não se editam; commit nunca quebra produção.
5. **Modular desde o nascimento** — código pronto pra escalar, documentação viva.
