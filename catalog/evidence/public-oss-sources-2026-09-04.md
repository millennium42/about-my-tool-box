# Evidência E1: fontes públicas e licenças

Em 2026-09-04, as alternativas open source e as entradas cuja licença precisava ser
resolvida foram consultadas diretamente no GitHub. O repositório canônico estava
público e não arquivado; a licença indicada foi lida no arquivo de licença da
origem. Isso sustenta E1, não funcionamento ou equivalência.

| Repositório canônico | Estado observado | Licença observada |
|---|---|---|
| [podman-desktop/podman-desktop](https://github.com/podman-desktop/podman-desktop) | Público, não arquivado | Apache-2.0 |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | Público, não arquivado | MIT |
| [woodpecker-ci/woodpecker](https://github.com/woodpecker-ci/woodpecker) | Público, não arquivado | Apache-2.0 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Público, não arquivado | MIT |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Público, não arquivado | Apache-2.0, arquivo `LICENSE.txt` |
| [cline/cline](https://github.com/cline/cline) | Público, não arquivado | Apache-2.0 |
| [ollama/ollama](https://github.com/ollama/ollama) | Público, não arquivado | MIT |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Público, não arquivado | MIT |
| [valkey-io/valkey](https://github.com/valkey-io/valkey) | Público, não arquivado | BSD-3-Clause, arquivo `COPYING` |
| [uptrace/uptrace](https://github.com/uptrace/uptrace) | Público, não arquivado | AGPL-3.0 |
| [coollabsio/coolify](https://github.com/coollabsio/coolify) | Público, não arquivado | Apache-2.0 |
| [apache/cloudstack](https://github.com/apache/cloudstack) | Público, não arquivado | Apache-2.0 |
| [supabase/supabase](https://github.com/supabase/supabase) | Público, não arquivado | Apache-2.0 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Público, não arquivado | MIT |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Público, não arquivado | AGPL-3.0 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | Público, não arquivado | MIT |
| [getmaxun/maxun](https://github.com/getmaxun/maxun) | Público, não arquivado | AGPL-3.0 |
| [apify/crawlee](https://github.com/apify/crawlee) | Público, não arquivado | Apache-2.0 |
| [osm-search/Nominatim](https://github.com/osm-search/Nominatim) | Público, não arquivado | Python sob GPL-3.0-or-later; Lua para osm2pgsql sob Apache-2.0; demais arquivos sob GPL-2.0; dados OpenStreetMap sob ODbL |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | Público, não arquivado | MIT |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Público, não arquivado | Transição MIT/Apache-2.0; documentação sob CC-BY-4.0 conforme a origem |
| [espocrm/espocrm](https://github.com/espocrm/espocrm) | Público, não arquivado | AGPL-3.0, arquivo `LICENSE.txt` |
| [searxng/searxng](https://github.com/searxng/searxng) | Público, não arquivado | AGPL-3.0 |
| [getprobe-dev/probe-extension](https://github.com/getprobe-dev/probe-extension) | Público, não arquivado | AGPL-3.0 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Público, não arquivado; branch padrão `v8` | Apache-2.0 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Público, não arquivado | MIT |
| [blader/humanizer](https://github.com/blader/humanizer) | Público, não arquivado | MIT |

## Fonte pública que não é OSS

| Repositório canônico | Estado observado | Licença/modelo | Tratamento no catálogo |
|---|---|---|---|
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | Público, não arquivado | [MIT + Commons Clause](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md); source-available | Não chamar de OSS; comparar com [shadcn/ui](https://github.com/shadcn-ui/ui) e conferir a restrição antes de redistribuir componentes |

A checagem não auditou dependências, marcas, patentes, segurança, releases nem
adequação jurídica. Repita a consulta antes da adoção e valide a licença do commit
realmente fixado pelo projeto.
