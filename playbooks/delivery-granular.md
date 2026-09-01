# Playbook: entrega granular

## Objetivo

Entregar uma mudança pequena, revisada e demonstrável, sem confundir um recorte
técnico fechado com o produto inteiro pronto.

## Procedimento

1. Registrar objetivo, escopo, fora de escopo e critérios de aceite.
2. Inspecionar estado atual, branch, remoto, testes e CI antes de confiar em uma
   anotação anterior.
3. Criar uma tarefa focal e uma verificação que falhe pelo motivo esperado.
4. Implementar somente o requisito da tarefa.
5. Executar a verificação até ficar verde.
6. Fazer review independente contra cada critério.
7. Atualizar código, documentação, migração, reset/seed e contagens afetadas juntos.
8. Fazer commit pequeno e registrar evidência, riscos e próximo recorte.

## Não encerrar como pronto quando

Ainda faltam integração de fluxo, decisão de produto, UI, demo, documentação,
migração, CI ou evidência visual. Escreva exatamente o que foi fechado e o que está
pendente.
