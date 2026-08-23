# Princípios de Trabalho (universais)

Princípios que aplico em **qualquer** projeto. Regras operacionais, não teoria.
Inspirados em Ponytail (YAGNI) e no ecossistema de agentes de
https://github.com/DietrichGebert/ponytail.

## 1. Ponytail (YAGNI aplicado)
> "The best code is the code you never wrote." — DietrichGebert/ponytail

O agente deve pensar como o **dev sênior mais preguiçoso da sala**: resolver o
problema com o menor esforço possível, preferindo recursos nativos a dependências.

- Codar o **mínimo necessário** que resolve o problema real.
- Ordem de preferência para resolver algo:
  `stdlib` > `dependência leve` > `implementação mínima própria`.
- Marcar atalho intencional com comentário `ponytail:` para revisão futura.
- Não adicionar feature "por via das dúvidas" — só o que o requisito pede.
- Antes de instalar uma lib: perguntar "o stdlib/plataforma nativa já faz isso?".

**Referência:** https://github.com/DietrichGebert/ponytail
**Variantes do ecossistema:**
- `m1nd` — primeira camada de orientação estrutural antes de grep/leitura ampla.
- `rtk` — wrapper de shell; prefixar comandos com `rtk`; `rtk proxy` p/ raw output;
  `rtk graphify query|path|explain` p/ navegar o grafo de código.
- `probe` — revisão de código por IA em PRs (https://github.com/getprobe-dev/probe-extension).

## 2. Qualidade de Código e Engenharia
- **TDD quando fizer sentido** — em greenfield, RED-GREEN-REFACTOR. Em projeto
  legado, teste antes de corrigir regressão.
- **Modularidade desde o nascimento** — separar em pastas/responsabilidades claras.
- **Documentação Viva** — documentar enquanto se constrói. Commits granulares
  exigem atualizar `README.md` / `CLAUDE.md` / `skills.md` junto.
- **Entregas (CI/CD)**: meta P0=0, P1=0 (zero bugs críticos/altos).
  Commit **nunca** quebra o estado funcional de produção.
- **Cobertura de testes** ≥ 80% onde fizer sentido.

## 3. Segurança & Compliance
- **Zero PII em logs** de sistema. Pseudonimizar (hash/links internos) quando precisar
  rastrear, em vez de expor dado pessoal.
- **Base legal** para contato/outreach B2B: interesse legítimo + opt-out obrigatório
  e respeitado. (Ex.: LGPD Art. 7º II — adaptar à jurisdição do projeto.)
- **Proibido em produção**:
  - NUNCA usar mocks em ambiente de produção.
  - NUNCA editar migrations de DB já aplicadas (só aditivas).
  - NUNCA inventar dados (leads, depoimentos, números, endereços, notas).
  - NUNCA expor API keys / tokens / senhas em doc ou commit.

## 4. Finishing the Job
- O entregável é um **artefato funcionando com output real de execução**, não um stub.
- Se uma tool/install/network falha e bloqueia o caminho real, digo HONESTAMENTE o
  que falhou — não fabrico saída plausível.
- Executo até o fim sem parar para confirmar a cada passo (exceto ações destrutivas).

## 5. Verificação Honesta
- Não afirmo que X funciona sem evidência (execução real, log, status code).
- Claims verificáveis (ex.: "número existe") exigem método comprovado — senão rotulo
  como "alta probabilidade + verificação manual".
- Diferenciar: output de ferramenta real ≠ suposição.

## 6. Graphify como mapa persistente do projeto
> https://github.com/Graphify-Labs/graphify

Tratar o grafo de código como mapa persistente do projeto:
- Construir cedo (`graphify extract . --out .`), consultar antes de navegação ampla,
  manter fresco após mudanças (`graphify update .`).
- `graphify query "<pergunta>"` para arquitetura/relacionamentos/dono de arquivo/fluxo.
- `graphify path "<A>" "<B>"` para dependências/pontes entre conceitos.
- `graphify explain "<conceito>"` para refresh focado.
- ~160x mais eficiente que grep; menos falsos positivos.
