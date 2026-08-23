# Metodologia de Trabalho (Ralph Loop)

Workflow padrão para garantir qualidade, escopo definido e foco.
Bloqueia escopo extra e garante previsibilidade.
(Origem: https://github.com/snarktank/ralph — "Ralph is an autonomous AI agent
loop that runs repeated...". ⭐ 21k+.)

## 1. Planejar (`/spec`)
Entender o que precisa ser feito via perguntas precisas (uma por vez).
- Entender: objetivo, requisitos indispensáveis, restrições, definição de "concluído".
- Resultado salvo em `specs/nome-feature.md` (usar `projects/spec-template.md`).
- **NÃO CONSTRUIR NESTA FASE.**

## 2. Executar (`/build`)
Desenvolver seguindo a spec com rigor.
- Ler a spec de ponta a pena.
- Construir **EXATAMENTE** conforme a spec. Sem features extras, sem refactor não pedido.
- Listar requisitos atendidos ao terminar.

## 3. Revisar (`/review`)
Validar se o construído condiz com a spec.
- Comparar código contra cada requisito.
- Listar lacunas, bugs, faltantes. Rejeitar se < 100%.
- Aprovar apenas quando completo.
- Reportar o que foi **provado diretamente** vs o que foi **inferido** de docs/grafo.

## 4. Aprender
Retroalimentação. Habilidades de uso recorrente viram `skills` globais reutilizáveis.

---

## Speed modes (do ecossistema Ponytail/rtk)
- **Light mode**: tarefas locais triviais → `rtk` + `Ponytail` sem ritual extra.
- **Structural mode**: arquitetura, domínio, review, finanças, integração ou edições
  arriscadas → `rtk` + `m1nd` + `Graphify` + `Ponytail`.

---

## Outros Loops / Metodologias de referência
- **Superpowers** (https://github.com/obra/superpowers — ⭐ 276k+):
  "An agentic skills framework & software development method."
  Workflow: Brainstorm → TDD → Subagent → Review → Ship.
- **Ruflo** (https://github.com/ruvnet/ruflo — ⭐ 68k+):
  "The original agent meta-harness. Deploy intelligent multi-agent swarms..."
  Memória HNSW auto-aprendizado, swarms.
- **GStack**: pack de ferramentas com checagens CSO (OWASP Top 10 + STRIDE).
- **Humanizer** (https://github.com/blader/humanizer — ⭐ 37k+):
  "Agent skill that removes signs of AI-generated writing...".
  Substituições determinísticas (jargão → linguagem cotidiana). Útil em qualquer
  comunicação automatizada (e-mails, mensagens, UX copy). Ver `methodologies/humanizer.md`.
