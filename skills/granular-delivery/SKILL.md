---
name: granular-delivery
description: Entregar mudanças pequenas com teste, review, documentação e evidência.
---

# Entrega granular

Use quando a mudança tiver risco, integração, banco, segurança ou mais de um
critério de aceite.

## Procedimento

1. Inspecione status, branch, remoto, testes e CI atuais.
2. Separe uma unidade focal e escreva a verificação esperada.
3. Implemente somente a unidade da spec.
4. Execute a verificação e registre a saída.
5. Faça review independente contra cada requisito.
6. Atualize testes, migrations, seeds, documentação e evidência afetados.
7. Registre o que foi fechado e o que continua pendente.

Não chame um recorte técnico de produto inteiro pronto sem verificar integração,
UI, operação, documentação e os critérios de demonstração aplicáveis.
