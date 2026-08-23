# Metodologia de Trabalho (Ralph Loop)

Workflow padrão que uso para garantir qualidade, escopo definido e foco.
Bloqueia escopo extra e garante previsibilidade. Originado de

## 1. Planejar (`/spec`)
Entender o que precisa ser feito via perguntas precisas (uma por vez).
- Entender: objetivo, requisitos indispensáveis, restrições, definição de "concluído".
- Resultado salvo em `specs/nome-feature.md`.
- **NÃO CONSTRUIR NESTA FASE.**

## 2. Executar (`/build`)
Desenvolver seguindo a spec com rigor.
- Ler `specs/nome-feature.md` de ponta a ponta.
- Construir **EXATAMENTE** conforme a spec. Sem features extras, sem refactor não pedido.
- Listar requisitos atendidos ao terminar.

## 3. Revisar (`/review`)
Validar se o construído condiz com a spec.
- Comparar código contra cada requisito.
- Listar lacunas, bugs, faltantes. Rejeitar se < 100%.
- Aprovar apenas quando completo.

## 4. Aprender
Retroalimentação. Habilidades de uso recorrente viram `skills` globais.

---

## OUTROS LOOPS / METODOLOGIAS QUE USO

### Humanizer (tom humano)
- `github.com/blader/humanizer` — deixa mensagem com tom humano, sem jeito de robô.
- Aplicado em prospecção B2B (WhatsApp). Substituições determinísticas:
  jargão → linguagem cotidiana, quebra parágrafos longos, pausas naturais.
- Princípio: copy direta, útil, SEM robótico, sem encher de adjetivos.

Pipeline real, testado end-to-end:
```
Google Maps Scraper (Docker, porta 8081)
   → CSV de leads (nome, phone, site, categoria, endereço, lat/lon)
   → Filtro: sem site próprio + (celular PJ ou perfil social) + NÃO franquia
   → Crawl4AI (Docker unclecode/crawl4ai, porta 11235) abre perfis sociais
       procura wa.me / api.whatsapp / agrupadores (linktr.ee, beacons, bio.link)
   → Hermes qualifica (ranqueia por probabilidade de compra)
   → CrewAI (MCP) ranqueia + redige abordagem
   → Dispara WhatsApp (apenas números CONFIRMADOS)
```
- Scoring usado: +30 sem site, +30 sem software visível, +20 rating≥4.0 sem site,
  -50 franquia (decisão centralizada).

### Superpowers / Ruflo / GStack (referência)
- **Superpowers** (github.com/obra/superpowers): Brainstorm → TDD → Subagent → Review → Ship.
- **Ruflo** (github.com/ruvnet/ruflo): Meta-harness, swarms, memória HNSW auto-aprendizado.
- **GStack**: +23 ferramentas, checagens CSO (OWASP Top 10 + STRIDE).
