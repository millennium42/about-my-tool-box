# Playbook: migrações e contratos de dados

1. Definir o contrato e a regra de negócio antes da tabela.
2. Criar migration aditiva; não editar migration já aplicada.
3. Atualizar reset, seed, contagens e testes que dependem do esquema.
4. Validar chaves, unicidade, limites numéricos, nulos e índices.
5. Testar autorização, idempotência, transação e concorrência quando aplicável.
6. Exercitar o fluxo completo que consome o dado, não apenas o insert.
7. Documentar origem, destino, retenção, custo, auditoria e comportamento de erro.
8. Confirmar CI e o estado do banco no commit atual.

Se a funcionalidade tem UI ou integração externa, a conclusão do schema não encerra
o trabalho de produto.
