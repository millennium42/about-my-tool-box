# Toolchain de base: Windows + WSL2

Windows com WSL2 é o caminho primário desta base. Linux e macOS continuam
suportados como ambientes secundários. As versões executadas estão em
[evidence/base-toolchain.md](../catalog/evidence/base-toolchain.md).

## Componentes

| Ferramenta | Fonte e instalação | Verificação mínima |
|---|---|---|
| Git | [git-scm.com/downloads](https://git-scm.com/downloads) | `git --version`, clone e status |
| Python | [python.org/downloads](https://www.python.org/downloads/) ou pacote da distribuição WSL | `python3 --version` e script mínimo |
| Node.js/npm | [nodejs.org/download](https://nodejs.org/en/download) | `node --version`, `npm --version` e script mínimo |
| Docker Engine | [documentação oficial](https://docs.docker.com/engine/install/) | `docker version` e container descartável |
| Docker Compose | [documentação oficial](https://docs.docker.com/compose/) | `docker compose version` e stack mínima |
| GitHub Actions | [documentação oficial](https://docs.github.com/actions) | workflow no commit atual |

Docker Desktop tem condições comerciais próprias. Compare com
[Podman Desktop](https://github.com/podman-desktop/podman-desktop) e leia
[serviços pagos](../catalog/paid-services.md) antes de padronizar.

## Preparação do WSL2

No PowerShell com privilégios adequados:

```powershell
wsl --install
wsl --status
wsl --list --verbose
```

Reinicialização e escolha de distribuição podem ser necessárias. Siga a
[documentação da Microsoft](https://learn.microsoft.com/windows/wsl/install).

Na distribuição WSL baseada em Ubuntu, um início comum é:

```bash
sudo apt update
sudo apt install git python3 python3-venv
git --version
python3 --version
```

Para Node, use uma versão LTS suportada conforme a
[documentação oficial](https://nodejs.org/en/download/package-manager). Para
containers, escolha conscientemente entre integração do Docker Desktop com WSL2,
Docker Engine dentro do Linux ou Podman; documente qual daemon e contexto estão
ativos.

## Limites entre Windows e Linux

- Mantenha projetos Linux no filesystem do WSL2 para evitar desempenho e permissões
  inconsistentes.
- Instale dependências dentro do ambiente que vai executá-las.
- Não compartilhe `node_modules`, `.venv`, sockets ou caches entre Windows e WSL2.
- Confirme `which`, versões, diretório e contexto Docker antes de diagnosticar código.
- Não publique caminhos locais em logs ou documentação.

## Verificação do projeto

Registre em arquivo privado ou sanitizado:

```bash
uname -a
git --version
python3 --version
node --version
npm --version
docker version
docker compose version
git status --short --branch
```

Não copie saídas que revelem nome da máquina, usuário, IP, repositório privado ou
credenciais. Em Linux/macOS nativos, aplique as mesmas verificações usando a
instalação oficial adequada ao sistema.
