# Playbook: dados, retenção e privacidade

1. Definir quais dados existem, por que são necessários, quem pode acessá-los e por
   quanto tempo.
2. Separar preview somente leitura de aplicação efetiva.
3. Tornar a aplicação transacional, idempotente e reexecutável com segurança.
4. Preservar somente identificadores, hashes e evidências necessários ao contrato.
5. Registrar falhas externas como estado retryable, sem mascarar sucesso.
6. Testar o contrato completo de integração, não apenas um identificador parcial.
7. Validar logs, backups, exclusão, anonimização, autorização e base legal aplicável.

Retenção, eliminação e restauração precisam ser decisões de produto e compliance,
não apenas tarefas de banco.
