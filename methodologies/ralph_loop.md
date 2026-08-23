# Metodologia de Trabalho (Ralph Loop)

O **Ralph Loop** é o workflow padrão que utilizo para garantir qualidade, escopo bem definido e foco extremo. Ele bloqueia escopo extra e garante previsibilidade.

## 1. Planejar (`/spec`)
O primeiro passo de qualquer tarefa é entender o que precisa ser feito através de perguntas precisas.
- Entrevistar requisitos (uma pergunta por vez).
- Entender: objetivo, requisitos indispensáveis, restrições, definição de "concluído".
- O resultado é salvo em `specs/nome-feature.md`.
- **NÃO COMEÇAR A CONSTRUIR NESTA FASE.**

## 2. Executar (`/build`)
Desenvolver a funcionalidade seguindo a especificação com rigor.
- Ler `specs/nome-feature.md` de ponta a ponta.
- Construir **EXATAMENTE** conforme a spec.
- Sem features extras, sem refatorações não solicitadas.
- Listar requisitos atendidos ao terminar.

## 3. Revisar (`/review`)
Validar se o que foi construído condiz com a spec acordada.
- Comparar o código feito contra cada requisito do arquivo de spec.
- Listar lacunas, bugs, itens faltantes.
- Rejeitar se não estiver 100% atendido.
- Aprovar apenas quando completo.

## 4. Aprender
Retroalimentação do processo. 
- Habilidades adquiridas de uso recorrente tornam-se novas "skills" globais (`skills.md`).

## Outros Loops Especializados
- **Ruflo** (github.com/ruvnet/ruflo): Meta-harness, swarms, memória HNSW para auto-aprendizado.
- **Superpowers** (github.com/obra/superpowers): Workflow (Brainstorm → TDD → Subagent → Review → Ship).
- **GStack**: Pack de +23 ferramentas, incluindo verificações CSO de segurança (OWASP Top 10 + STRIDE).
