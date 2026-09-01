# Kit de ferramentas verificado

Esta é a base mínima testada para operar o catálogo no Windows nativo, Windows com
WSL2, Linux e macOS. A instalação deve ser feita pelas fontes oficiais.

| Ferramenta | Instalação oficial | Verificação mínima |
|---|---|---|
| Git | [git-scm.com/downloads](https://git-scm.com/downloads) | `git --version` e `git clone` |
| Python | [python.org/downloads](https://www.python.org/downloads/) | `python --version` e execução de script |
| Node.js | [nodejs.org/download](https://nodejs.org/en/download) | `node --version` e `npm --version` |
| Docker | [docs.docker.com/get-docker](https://docs.docker.com/get-docker/) | `docker --version` e `docker info` |
| Docker Compose | [docs.docker.com/compose](https://docs.docker.com/compose/) | `docker compose version` |

## Instalação por ambiente

Use os comandos abaixo como ponto de partida e confirme a versão estável indicada
na documentação oficial. Gerenciadores podem variar por distribuição e por data.

### Windows nativo

```powershell
winget install --id Git.Git -e
winget install --id OpenJS.NodeJS.LTS -e
winget install --id Docker.DockerDesktop -e
```

Instale Python pelo [download oficial para Windows](https://www.python.org/downloads/windows/)
ou pelo instalador Python disponível no `winget`; habilite o launcher e valide
`python --version` depois da instalação.

### Windows com WSL2

Instale o WSL2 conforme a [documentação da Microsoft](https://learn.microsoft.com/windows/wsl/install),
ative a integração da distribuição no Docker Desktop e instale Git/Python dentro
da distribuição. Para Node.js, use a [documentação oficial de instalação](https://nodejs.org/en/download/package-manager)
ou um gerenciador de versões mantido; não reutilize `node_modules` do Windows.

### Linux

Use o gerenciador da distribuição para Git e Python e siga a documentação oficial
para Node.js e Docker Engine/Desktop. Depois confirme todos os comandos da tabela.

### macOS

Com Homebrew instalado, uma opção é:

```bash
brew install git python node
brew install --cask docker
```

Use o [guia oficial do Docker para macOS](https://docs.docker.com/desktop/setup/install/mac-install/)
quando preferir o instalador gráfico.

## Política de versões

Use uma versão LTS ou estável suportada pela ferramenta. Não fixe uma versão no
catálogo sem registrar a data e a fonte. A versão observada nesta revisão foi:

```text
git 2.55.0.windows.5
Python 3.13.15
Node.js v26.7.0
npm 11.19.0
Docker 29.7.2
Docker Compose v5.4.0
```

Data da coleta: 2026-09-01. Esses números são evidência do ambiente de revisão,
não uma exigência universal.
Repita os comandos acima no seu computador.

## Windows com WSL2

Escolha um ambiente por execução. Para Node, npm, bancos e testes Linux, prefira
um diretório dentro do filesystem do WSL; não misture `node_modules` entre Windows
e Linux. O Docker Desktop pode ser integrado ao WSL2, mas a distribuição e o
filesystem continuam fazendo parte do diagnóstico.
