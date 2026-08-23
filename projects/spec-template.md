# Template — Spec de Projeto / Feature

Copie para `specs/<nome>.md` ao iniciar um projeto ou feature (Ralph Loop /spec).
Preencha tudo antes de construir. Base: https://github.com/snarktank/ralph.

```markdown
# <Nome do Projeto / Feature>

## Objetivo
Em 1–2 frases: o que resolve e para quem.

## Requisitos indispensáveis
- [ ] ...
- [ ] ...

## Restrições
- Stack obrigatória / proibida:
- Jurídico/compliance (LGPD/GDPR/outro):
- Prazo / orçamento:

## Definição de "Concluído"
- [ ] Critério verificável 1 (como provar que funciona)
- [ ] Critério verificável 2

## Stack (decisão) — aplicar Ponytail
- Frontend: (prefira stdlib/nativo)
- Backend:
- Banco:
- Infra:
- LLM/Agentes:

## Decisões / Regras de negócio
- Regra 1:
- Regra 2:

## Out of scope (explícito)
- O que NÃO será feito nesta iteração.

## Rejeição (P0/P1)
- P0: qualquer bug crítico / dado inventado / quebra de produção.
- P1: lentidão, a11y quebrada, CTA ineficaz.
```

---

# Template — Documentar projeto ativo (preencher após kickoff)

Copie para `projects/<nome>.md` quando o projeto estiver em andamento, para ser
o "cérebro" dele em sessões futuras.

```markdown
# <Nome do Projeto>

## Descrição
O que é, para quem, qual problema resolve.

## Status
(ativo / concluído / em espera / R&D)

## Stack
- ...
- Repositório: https://github.com/<org>/<repo> (se houver)

## Ferramentas de IA conectadas
- MCPs: ...
- Graphify: sim/não (graphify-out/)
- Ponytail/rtk/m1nd: sim/não

## Regras de negócio / Decisões
- ...

## Pitfalls conhecidos (não repetir)
1. ...

## Como rodar
\`\`\`bash
...
\`\`\`

## Artefatos obrigatórios (seed)
- docs/contexto-operacional.md
- AGENTS.md / CLAUDE.md
- specs/
- skills/ , workflows/
```
