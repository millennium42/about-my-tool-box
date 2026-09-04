# Perfil: automação e dados

## Início mínimo

- Git;
- Python e `venv`;
- biblioteca padrão sempre que suficiente;
- entrada e saída com contrato explícito;
- teste de reexecução e falha parcial;
- armazenamento e retenção definidos antes da coleta.

Adicione pytest e Ruff depois de validá-los no ambiente. Docker entra quando houver
um serviço externo reproduzível; fila ou orquestrador entra somente quando execução
local ou agendada simples não cumprir volume, concorrência ou retry.

## Dados

Use amostras fictícias inequívocas. Registre origem, finalidade, chave de
idempotência, deduplicação, acesso, retenção e exclusão. Logs devem preservar estado
técnico suficiente sem payload pessoal.

## Verificação mínima

1. criar ambiente limpo;
2. executar caso feliz;
3. executar entrada inválida e falha externa;
4. repetir para provar idempotência;
5. inspecionar saída e logs por dados sensíveis;
6. confirmar código de saída, documentação e CI.

Para scheduler, storage, fila ou observabilidade pagos, registre uma alternativa OSS
e a carga operacional correspondente.
