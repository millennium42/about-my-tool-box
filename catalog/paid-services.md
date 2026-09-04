# Serviços pagos ou híbridos e alternativas open source

Consulta das fontes públicas realizada em 2026-09-04, registrada em
[evidence/public-oss-sources-2026-09-04.md](evidence/public-oss-sources-2026-09-04.md).
Esta tabela não afirma equivalência: uma solução self-hosted troca parte do preço do fornecedor por
infraestrutura, atualização, backup, observabilidade e resposta a incidentes.

Antes de escolher, compare dados enviados, região, retenção, SLA, lock-in, licença,
recursos ausentes e capacidade real da equipe de operar a alternativa.

| Serviço e modelo | Uso | Alternativa OSS pública no Git | Licença da alternativa | Diferença essencial |
|---|---|---|---|---|
| [Docker Desktop](https://www.docker.com/pricing/) — Híbrido | Ambiente gráfico de containers | [Podman Desktop](https://github.com/podman-desktop/podman-desktop) | Apache-2.0 | Compatibilidade e integração não são idênticas; valide Compose, volumes e rede |
| [GitHub](https://github.com/pricing) — Híbrido | Hospedagem Git, issues e pull requests | [Gitea](https://github.com/go-gitea/gitea) | MIT | Exige hospedagem, backup, atualização e segurança próprios; integrações e UX diferem |
| [GitHub Actions](https://github.com/pricing) — Híbrido | CI/CD hospedado | [Woodpecker CI](https://github.com/woodpecker-ci/woodpecker) | Apache-2.0 | Exige servidor, runners, atualização e operação próprios |
| [Codex](https://openai.com/codex/) — Pago/Híbrido | Agente de desenvolvimento | [OpenHands](https://github.com/OpenHands/OpenHands) | MIT | Modelos, sandbox, UX, integrações e operação diferem |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code/costs) — Pago/Híbrido | Agente de desenvolvimento em terminal, IDE, desktop e web | [Aider](https://github.com/Aider-AI/aider) | Apache-2.0 | Fluxo, modelos, permissões, memória e integrações diferem; modelo local exige configuração própria |
| [Cursor](https://cursor.com/pricing) — Freemium/Híbrido | Editor e agentes de desenvolvimento | [Cline](https://github.com/cline/cline) | Apache-2.0 | Não substitui o editor completo nem os serviços cloud; modelo/API podem continuar pagos |
| [OpenAI API](https://openai.com/api/pricing/) — Pago | Modelos por API | [Ollama](https://github.com/ollama/ollama) ou [llama.cpp](https://github.com/ggml-org/llama.cpp) | MIT | Modelo local pode ter menor capacidade; exige hardware, serving e avaliação próprios |
| [Upstash](https://upstash.com/pricing) — Híbrido | Dados serverless e filas | [Valkey](https://github.com/valkey-io/valkey) | BSD-3-Clause | Não inclui plataforma serverless gerenciada, cobrança por uso nem operação automática |
| [Sentry Cloud](https://sentry.io/pricing/) — Híbrido | Erros e observabilidade | [Uptrace](https://github.com/uptrace/uptrace) | AGPL-3.0 | Instrumentação, UX, integrações, escala e suporte diferem |
| [Render](https://render.com/pricing) — Híbrido | Deploy gerenciado | [Coolify](https://github.com/coollabsio/coolify) | Apache-2.0 | Requer servidor e responsabilidade operacional; serviços gerenciados não são equivalentes |
| [Vercel](https://vercel.com/pricing) — Híbrido | Frontend e funções gerenciadas | [Coolify](https://github.com/coollabsio/coolify) | Apache-2.0 | CDN, runtime serverless, previews e integração com framework diferem |
| [AWS](https://aws.amazon.com/pricing/) — Pago | Cloud e serviços gerenciados | [Apache CloudStack](https://github.com/apache/cloudstack) | Apache-2.0 | É uma plataforma IaaS própria, não substitui o catálogo de serviços AWS |
| [Supabase Cloud](https://supabase.com/pricing) — Híbrido | Backend gerenciado | [Supabase self-hosted](https://github.com/supabase/supabase) | Apache-2.0 | Backup, upgrades, e-mail, storage, observabilidade e SLA ficam com a equipe |
| [Browser Use Cloud](https://browser-use.com/) — Híbrido | Browsers para agentes | [Browser Use](https://github.com/browser-use/browser-use) | MIT | A biblioteca não fornece automaticamente browsers remotos, proxies e operação gerenciada |
| [Firecrawl Cloud](https://www.firecrawl.dev/pricing) — Híbrido | Crawling e extração por API | [Firecrawl self-hosted](https://github.com/firecrawl/firecrawl) | AGPL-3.0 | Escala, filas, proxies e manutenção passam para o operador |
| [Dify Cloud](https://dify.ai/pricing) — Híbrido/source-available | Workflows e aplicações de IA | [Langflow](https://github.com/langflow-ai/langflow) | MIT | Componentes, conectores e runtime diferem; a licença do Dify contém condições adicionais |
| [Maxun Cloud](https://www.maxun.dev/) — Híbrido | Extração visual | [Maxun self-hosted](https://github.com/getmaxun/maxun) | AGPL-3.0 | Execução, browsers, proxies e atualização ficam com a equipe |
| [Apify](https://apify.com/pricing) — Híbrido | Crawlers, actors e infraestrutura | [Crawlee](https://github.com/apify/crawlee) | Apache-2.0 | Crawlee é biblioteca; não inclui marketplace, scheduler e infraestrutura gerenciada |
| [Google Maps Platform](https://mapsplatform.google.com/pricing/) — Pago/Híbrido | Busca de locais e geocodificação | [Nominatim](https://github.com/osm-search/Nominatim) com dados OpenStreetMap | Código sob GPL-3.0-or-later, GPL-2.0 e Apache-2.0; dados sob ODbL | Cobertura, ranking, POIs e APIs diferem; uso público ou self-hosting tem políticas e operação próprias |
| [21st.dev](https://21st.dev/) — Híbrido | Geração e descoberta de UI | [shadcn/ui](https://github.com/shadcn-ui/ui) | MIT | Biblioteca de componentes não substitui geração por IA nem catálogo hospedado |
| [Context7](https://context7.com/) — Híbrido | Documentação atual para agentes | [Fetch MCP](https://github.com/modelcontextprotocol/servers) + documentação oficial | MIT/Apache-2.0 em transição | Não há índice curado equivalente; segurança e qualidade das fontes ficam com o projeto |
| [Twenty Cloud](https://twenty.com/pricing) — Híbrido | CRM gerenciado | [EspoCRM](https://github.com/espocrm/espocrm) | AGPL-3.0 | Modelo de dados, UX, integrações e migração não são equivalentes |
| [Perplexity API](https://www.perplexity.ai/api-platform) — Pago | Pesquisa com modelo e citações | [SearXNG](https://github.com/searxng/searxng) | AGPL-3.0 | Metabusca não fornece a mesma síntese, ranking ou contrato de API; um adaptador MCP é separado |

## Regra para novas entradas

Uma contribuição que citar serviço pago, freemium, trial ou plano hospedado deve:

1. adicionar ou atualizar uma linha acima;
2. apontar para um repositório público específico, não para uma busca ou perfil;
3. confirmar que o repositório não está arquivado e registrar a licença;
4. declarar a data da consulta e a diferença funcional;
5. marcar “nenhuma alternativa adequada encontrada” quando esse for o resultado,
   sem inventar equivalência.

Alternativas desta página são E1 até serem executadas no projeto escolhido.
