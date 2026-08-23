# Filosofias de Trabalho

Minhas filosofias centrais focam em escalabilidade desde o início, qualidade máxima, e compliance rigoroso.

## Ponytail (YAGNI)
- Codar o mínimo necessário.
- **Ordem de prioridade**: `stdlib` > `dependência` > `implementação mínima`.
- Marcar atalhos intencionais com `ponytail:` em comentário para futura revisão.

## Qualidade de Código e Engenharia
- **TDD (Test-Driven Development)**: Utilizado desde o primeiro PR.
- **Modularidade**: O código deve nascer pronto para escalar.
- **Documentação Viva**: Documentar simultaneamente ao desenvolvimento. Commits granulares exigem atualizações nos arquivos de documentação (`skills.md`, `CLAUDE.md`, etc).
- **Entregas (CI/CD)**: A meta é sempre P0=0, P1=0 (zero bugs críticos/altos). Um commit **nunca** pode quebrar o estado funcional da produção. Cobertura de testes ≥ 80%.

## Segurança & Compliance
- **Auditoria**: Modelo *append-only* com `clientRequestId` obrigatório.
- **Privacidade (LGPD)**: ZERO PII em logs de sistema. Preferência clara por pseudonimização (linkage interno preservado) sobre anonimização simples.
- **Proibido em Produção**: Nunca usar mocks, nunca editar migrations de DB que já foram aplicadas.
- **Plugins Ativos**: Verificações automáticas de segurança rodam em todos os projetos, analisando secrets e credenciais antes de cada commit.
