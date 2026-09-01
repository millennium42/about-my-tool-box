# Playbook: Windows, WSL2 e repositórios

## Regra principal

Escolha um ambiente autoritativo para cada execução. Para projetos Node, npm,
Drizzle, testes e ferramentas Linux, prefira o filesystem nativo do WSL2. Não
compartilhe `node_modules` entre Windows e Linux.

## Procedimento

1. Confirmar branch, remoto e status no checkout correto.
2. Manter o clone Windows como origem de trabalho ou backup quando isso for exigido.
3. Sincronizar para um diretório Linux sem copiar `node_modules`, caches, cobertura,
   build ou `.git`.
4. Instalar dependências dentro do WSL2.
5. Executar testes isoladamente quando usam o mesmo banco ou estado compartilhado.
6. Registrar versão de Node, npm, Python, Docker e banco.
7. Não tratar erro de runtime misturado como falha do código antes de corrigir o
   ambiente.

## Sinais de ambiente incorreto

`node_modules/.bin` incompatível, testes que não encontram arquivos, lentidão anormal,
erro de permissão ou comandos usando o Node do Windows dentro de um caminho Linux.
