# Evidência: toolchain de base

Este registro limita exatamente o status E3. Ele não cobre as candidatas E1 do
catálogo nem garante compatibilidade com todo projeto.

## Execução em Windows

Coleta registrada em 2026-09-01 no ambiente de revisão:

| Comando | Resultado observado |
|---|---|
| `git --version` | `git version 2.55.0.windows.5` |
| `python --version` | `Python 3.13.15` |
| `node --version` | `v26.7.0` |
| `npm --version` | `11.19.0` |
| `docker --version` | `Docker version 29.7.2` |
| `docker compose version` | `Docker Compose version v5.4.0` |

Também foram registrados script mínimo em Python e Node, `docker info` e validação
do repositório. Não foi preservada evidência de um container e uma stack Compose
mínimos; por isso Docker e Compose ficam E2. A coleta prova disponibilidade naquele
ambiente e naquela data; não prova WSL2 nem uma aplicação específica.

## Reexecução no ambiente de manutenção

Coleta em 2026-09-04, Linux x86_64:

| Comando | Resultado observado |
|---|---|
| `git --version` | `git version 2.51.1` |
| `python --version` | `Python 3.12.13` |
| `node --version` | `v24.19.0` |
| `npm --version` | `11.9.0` |
| script mínimo Node | `{"ok":true}` |
| `npm --offline init --yes` + `npm --offline pkg get name` | manifesto criado e nome lido com sucesso |
| script mínimo Python | `{"ok": true}` |
| `python scripts/verify_repository.py` | concluído sem falhas antes da alteração |
| `docker --version` | bloqueado: executável indisponível |
| `docker compose version` | bloqueado: Docker indisponível |

Docker e Compose permanecem E2: o daemon não está disponível nesta reexecução e o
registro Windows anterior não inclui uso mínimo suficiente. Revalide no ambiente do
projeto antes de depender deles.

## CI hospedado

O workflow multiplataforma do GitHub Actions executou com sucesso no commit raiz
sanitizado `ae6707a7a48272de3c355abda1d39118542c5330` em 2026-09-04:
[execução 33911252817](https://github.com/millennium42/about-my-tool-box/actions/runs/33911252817).

Os jobs de documentação passaram em `windows-latest`, `macos-latest` e
`ubuntu-latest`. Essa evidência cobre o conteúdo sanitizado desse commit; cada nova
alteração deve passar novamente por `.github/workflows/validate.yml`.
