# Playbook: verificação honesta

## Classifique cada afirmação

| Classe | Exemplo | Como tratar |
|---|---|---|
| Provado | teste executado e saída capturada | afirmar com contexto |
| Inferido | compatibilidade baseada em documentação | marcar como inferência |
| Não verificado | ferramenta apenas listada | não recomendar |
| Bloqueado | ambiente, credencial ou serviço ausente | registrar o bloqueio |

## Procedimento

1. Transformar a afirmação em um teste observável.
2. Executar em ambiente declarado.
3. Guardar comando, versão, resultado e data.
4. Repetir após mudanças relevantes.
5. Não usar estrela, marketing, mock ou código não executado como prova de funcionamento.

Uma execução verde valida aquele estado e aquele escopo; não valida automaticamente
integrações que não foram exercitadas.
