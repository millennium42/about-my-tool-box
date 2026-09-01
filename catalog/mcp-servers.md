# MCP servers

MCP é um protocolo de integração entre um cliente de IA e ferramentas ou fontes de
contexto. O protocolo não instala nenhum servidor por si só.

| Entrada | Função | Status | Observação |
|---|---|---|---|
| MCP Specification | Definir o protocolo | Em avaliação | Fonte oficial, não é um servidor instalável |
| Filesystem MCP | Acesso controlado a arquivos | Em avaliação | Confirmar implementação e permissões antes de usar |
| Fetch MCP | Consultas HTTP | Em avaliação | Restringir destinos e dados enviados |
| PostgreSQL MCP | Consultar banco | Em avaliação | Usar usuário de menor privilégio e somente leitura por padrão |
| Graphify | Contexto estrutural do código | Em avaliação | Validar CLI e formato de saída no projeto-alvo |
| Custom MCP/FastMCP | Expor API interna como tools | Em avaliação | Exigir autenticação, timeout, logs sem PII e teste e2e |
| Codebase Memory MCP | Memória de repositório | Em avaliação | Origem e instalação ainda precisam ser fixadas |
| Claude Mem | Memória entre sessões | Em avaliação | Confirmar se é skill, MCP ou produto antes de instalar |
| CrewAI MCP | Orquestração multiagente | Em avaliação | O exemplo conceitual não constitui implementação verificada |
| Perplexity MCP | Pesquisa externa | Em avaliação | Confirmar provedor, permissões e política de dados |
| Chrome DevTools MCP | Navegação/inspeção de browser | Em avaliação | Usar somente em sessão e páginas autorizadas |

## Configuração segura

1. Instalar pela fonte oficial e fixar a versão no projeto.
2. Registrar pelo mecanismo oficial do cliente de IA.
3. Passar segredos por ambiente ou gerenciador de segredos.
4. Conceder somente os diretórios, hosts e operações necessários.
5. Reiniciar o cliente e executar um teste mínimo observável.
6. Documentar a evidência no formato de [mcp-server-template.md](../mcp_servers/mcp-server-template.md).

Não use o exemplo de MCP como código de produção sem adicionar validação de
entrada, limites de tempo, tratamento de erro, autorização e testes.
