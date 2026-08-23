# Metodologia de Trabalho (Ralph Loop)

Workflow padrão para garantir qualidade, escopo definido e foco.
Bloqueia escopo extra e garante previsibilidade.
(Origem: `github.com/snarktank/ralph` — adaptado como framework genérico.)

## 1. Planejar (`/spec`)
Entender o que precisa ser feito via perguntas precisas (uma por vez).
- Entender: objetivo, requisitos indispensáveis, restrições, definição de "concluído".
- Resultado salvo em `specs/nome-feature.md` (usar `projects/spec-template.md`).
- **NÃO CONSTRUIR NESTA FASE.**

## 2. Executar (`/build`)
Desenvolver seguindo a spec com rigor.
- Ler a spec de ponta a ponta.
- Construir **EXATAMENTE** conforme a spec. Sem features extras, sem refactor não pedido.
- Listar requisitos atendidos ao terminar.

## 3. Revisar (`/review`)
Validar se o construído condiz com a spec.
- Comparar código contra cada requisito.
- Listar lacunas, bugs, faltantes. Rejeitar se < 100%.
- Aprovar apenas quando completo.

## 4. Aprender
Retroalimentação. Habilidades de uso recorrente viram `skills` globais reutilizáveis.

---

## Outros Loops / Metodologias de referência
- **Superpowers** (`github.com/obra/superpowers`): Brainstorm → TDD → Subagent → Review → Ship.
- **Ruflo** (`github.com/ruvnet/ruflo`): Meta-harness, swarms, memória HNSW auto-aprendizado.
- **GStack**: pack de ferramentas com checagens CSO (OWASP Top 10 + STRIDE).
- **Humanizer** (`github.com/blader/humanizer`): deixa copy/tons com tom humano,
  sem jeito de robô — substituições determinísticas (jargão → linguagem cotidiana).
  Útil em qualquer comunicação automatizada (e-mails, mensagens, UX copy).
