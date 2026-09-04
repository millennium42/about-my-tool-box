# Decisões mínimas de stack

Escolha pelo requisito, não pela popularidade. A tabela aponta um início pequeno; as
dependências em E1 precisam ser validadas no próprio projeto antes de virarem padrão.

| Cenário | Comece com | Adicione somente quando | Evite por padrão |
|---|---|---|---|
| Landing estática | HTML/CSS/JS; Vite se precisar de build | React quando houver estado e componentes reutilizáveis | SSR, banco e containers sem requisito |
| SPA web | Vite + TypeScript; React se a UI justificar | API e PostgreSQL quando houver persistência real | Next.js apenas por convenção |
| Web com SSR/full-stack TS | Next.js + TypeScript | PostgreSQL, auth e cache conforme requisitos | Redis/Valkey e Kubernetes antecipados |
| Admin em PHP | Laravel + PostgreSQL | Filament/Livewire para backoffice interativo | Microserviços sem escala comprovada |
| Automação | Python + `venv` + biblioteca padrão | pytest/Ruff; Docker para serviços externos | Fila e orquestrador para execução simples |
| IA | Python ou TypeScript + SDK direto | Ollama para execução local; MCP ou LangGraph para fluxo comprovado | Swarm, memória e múltiplos frameworks no início |
| Scraping autorizado | Cliente HTTP e parser | Playwright para páginas dinâmicas; Crawl4AI para extração assistida | Browser/agente quando HTTP basta |
| Documentos | Python + biblioteca do formato | renderização e inspeção visual | declarar qualidade só porque o arquivo abriu |
| Deploy pequeno | serviço gerenciado escolhido conscientemente | Coolify se a equipe aceitar self-hosting | Kubernetes para uma aplicação pequena |
| CRM | EspoCRM ou aplicação mínima do domínio | solução gerenciada se reduzir risco operacional | customização profunda antes de validar o processo |

## Ordem da decisão

1. Escolha um [perfil](../profiles/README.md).
2. Escreva a matriz da spec.
3. Consulte [tools.md](tools.md) para status e fonte.
4. Para custo hospedado, compare [paid-services.md](paid-services.md).
5. Execute E1/E2 em ambiente limpo e registre E3 no projeto.

Windows + WSL2 é o ambiente primário de orientação desta base. Mantenha dependências
Linux dentro do filesystem do WSL2 e não compartilhe `node_modules` entre sistemas.
