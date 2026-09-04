# MCP: protocolo, SDKs e servidores

MCP conecta um cliente de IA a ferramentas ou contexto. Citar um servidor não o
instala, não concede permissão e não demonstra que ele é seguro para produção.

Os servidores de referência oficiais são exemplos educacionais; a própria origem
alerta que eles não são soluções prontas para produção. Todos permanecem E1 nesta
base até um teste ponta a ponta no cliente e no ambiente escolhidos.

## Fontes canônicas

| Entrada | Uso | Status | Evidência | Fonte oficial | Limite principal |
|---|---|---|---|---|---|
| Especificação MCP | Contrato do protocolo | Referência | E1 | [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | Não é servidor instalável |
| SDK Python | Construir clientes e servidores | Em avaliação | E1 | [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | Validar versão estável e Python suportado |
| SDK TypeScript | Construir clientes e servidores | Em avaliação | E1 | [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | Validar versão estável e Node suportado |
| FastMCP | Servidores MCP em Python | Em avaliação | E1 | [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) | Camada adicional; não substitui autorização |
| Filesystem reference server | Arquivos com raízes limitadas | Em avaliação | E1 | [servidores oficiais](https://github.com/modelcontextprotocol/servers) | Exposição de arquivos e escrita precisam ser mínimas |
| Fetch reference server | Conteúdo HTTP | Em avaliação | E1 | [servidores oficiais](https://github.com/modelcontextprotocol/servers) | SSRF, conteúdo não confiável e exfiltração |
| Git reference server | Leitura e operações de Git | Em avaliação | E1 | [servidores oficiais](https://github.com/modelcontextprotocol/servers) | Limitar repositório e ações mutáveis |
| Memory reference server | Grafo de memória local | Em avaliação | E1 | [servidores oficiais](https://github.com/modelcontextprotocol/servers) | Retenção e remoção de contexto |
| Sequential Thinking reference server | Raciocínio estruturado | Em avaliação | E1 | [servidores oficiais](https://github.com/modelcontextprotocol/servers) | Exemplo educacional, sem garantia de qualidade |
| Time reference server | Datas e fusos | Em avaliação | E1 | [servidores oficiais](https://github.com/modelcontextprotocol/servers) | Confirmar timezone e relógio do host |
| Chrome DevTools MCP | Inspecionar Chrome | Em avaliação | E1 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Sessões, cookies e páginas podem conter dados sensíveis |
| Codebase Memory MCP | Indexar e consultar código | Em avaliação | E1 | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | Índice pode persistir código privado |
| Grok Mem, pacote `claude-mem` | Memória entre sessões | Em avaliação | E1 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Revisar armazenamento, retenção e clientes compatíveis |

O PostgreSQL reference server antigo aparece como arquivado na origem oficial e não
é recomendado. Consulte [retired.md](retired.md) em vez de copiar configurações
antigas. Para banco, prefira uma API estreita ou um servidor específico validado,
com usuário somente leitura e esquema permitido.

## Gate de instalação

1. Identifique cliente, servidor, versão, fonte e licença exatas.
2. Leia código/configuração e modele dados que podem sair do processo.
3. Fixe a versão; evite execução remota sem integridade verificável.
4. Conceda somente diretórios, hosts, comandos e métodos necessários.
5. Passe segredos por mecanismo próprio do cliente, nunca no Git.
6. Execute um caso permitido e um caso que deve ser negado.
7. Reinicie o cliente, repita o teste e registre a evidência pelo
   [template](../mcp_servers/mcp-server-template.md).

Serviço comercial acessado por MCP continua sujeito à regra de
[alternativa open source](paid-services.md). Um adaptador comunitário não transforma
o serviço subjacente em open source.
