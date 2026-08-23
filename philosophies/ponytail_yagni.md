# Filosofias de Trabalho

Princípios centrais que eu SIGO em qualquer projeto. Não são teoria — são regras
operacionais que já me quebraram a cara quando ignoradas.

## 1. Ponytail (YAGNI aplicado)
- Codar o **mínimo necessário** que resolve o problema real.
- Ordem de preferência para resolver algo:
  `stdlib` > `dependência leve` > `implementação mínima própria`.
- Marcar atalho intencional com comentário `ponytail:` para revisão futura.
- Não adicionar feature "por via das dúvidas" — só o que o requisito pede.

## 2. Qualidade de Código e Engenharia
- **TDD quando fizer sentido** — mas no meu fluxo, teste vem DEPOIS de correção
- **Modularidade desde o nascimento** — código deve nascer pronto para escalar,
  separado em pastas/responsabilidades (ver estrutura modular deste repo).
- **Documentação Viva** — documento enquanto construo. Commits granulares exigem
  atualizar `skills.md`, `CLAUDE.md`, `README.md` junto.
- **Entregas (CI/CD)**: meta P0=0, P1=0 (zero bugs críticos/altos).
  Commit **nunca** quebra o estado funcional de produção.

## 3. Segurança & Compliance (LGPD é sagrado)
- **Zero PII em logs de sistema.** Telefone vira SHA-256 em logs de envio.
- **Pseudonimização** (linkage interno preservado) > anonimização simples.
- **Interesse legítimo** (Art. 7º II LGPD) como base para prospecção B2B.
- Toda mensagem de prospecção inclui frase de opt-out:
  *"Se não fizer sentido, me avisa que eu não te chamo novamente."*
- Resposta de recusa = bloqueio permanente e irreversível do lead.

## 4. Proibido em Produção (hard rules)
- NUNCA usar mocks em ambiente de produção.
- NUNCA editar migrations de DB já aplicadas — só aditivas.
- NUNCA inventar dados (leads, depoimentos, números, endereços, notas).
- NUNCA expor API keys / tokens / senhas em arquivo de doc ou commit.

## 5. Finishing the Job (minha regra principal com IA)
- O entregável é um **artefato funcionando com output real de execução**, não um stub.
- Se uma tool/install/network falha e bloqueia o caminho real, digo HONESTAMENTE
  o que falhou — não fabrico saída plausível.
- Executo até o fim sem parar para confirmar a cada passo (a menos que destrutivo).

## 6. Honestidade de Verificação
- `wa.me/<num>` e `api.whatsapp.com/send?phone=` NÃO provam que o número existe
  (ambos retornam 200/302 mesmo com número falso).
- Confirmação automática confiável de WhatsApp = `wa.me` presente no PRÓPRIO perfil
  do Instagram da empresa. Demais = "alta probabilidade (celular PJ)" + verificação manual.
