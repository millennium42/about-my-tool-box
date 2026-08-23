# Princípios de Trabalho (universais)

Princípios que aplico em **qualquer** projeto. Regras operacionais, não teoria.

## 1. Ponytail (YAGNI aplicado)
- Codar o **mínimo necessário** que resolve o problema real.
- Ordem de preferência para resolver algo:
  `stdlib` > `dependência leve` > `implementação mínima própria`.
- Marcar atalho intencional com comentário `ponytail:` para revisão futura.
- Não adicionar feature "por via das dúvidas" — só o que o requisito pede.

## 2. Qualidade de Código e Engenharia
- **TDD quando fizer sentido** — em greenfield, RED-GREEN-REFACTOR. Em projeto
  legado, teste antes de corrigir regressão.
- **Modularidade desde o nascimento** — separar em pastas/responsabilidades claras.
- **Documentação Viva** — documentar enquanto se constrói. Commits granulares
  exigem atualizar `README.md` / `CLAUDE.md` / `skills.md` junto.
- **Entregas (CI/CD)**: meta P0=0, P1=0 (zero bugs críticos/altos).
  Commit **nunca** quebra o estado funcional de produção.

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
- Claims verificáveis (ex.: "número de WhatsApp existe") exigem método comprovado —
  senão rotulo como "alta probabilidade + verificação manual".
- Diferenciar: output de ferramenta real ≠ suposição.
