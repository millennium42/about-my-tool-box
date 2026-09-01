# Perfil: automação e dados

## Kit mínimo

- Git;
- Python;
- ambiente virtual ou gerenciador de dependências;
- testes para entradas, falhas e reexecução;
- armazenamento definido antes do script.

Docker entra quando a automação depende de banco, fila ou serviço externo. Uma fila
ou orquestrador só entra quando a execução local simples não atende ao requisito.

## Verificação mínima

Executar em ambiente limpo com dados de exemplo claramente marcados, repetir a
execução para verificar idempotência, conferir logs sem PII e guardar uma saída
reprodutível.
