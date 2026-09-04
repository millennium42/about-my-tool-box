# Primeiro projeto

Este roteiro leva uma ideia até a primeira tarefa verificável. Para a condução
completa por um agente, use também
[desenvolvimento guiado por IA](ai-guided-development.md).

## 1. Comece pela entrevista

Informe o que já sabe: problema, usuários, resultado, prazo, ambiente, dados e
orçamento. O agente deve perguntar somente o que ainda mudaria escopo, stack, custo,
privacidade ou aceite. Use [o modelo](../projects/interview-template.md).

## 2. Salve a spec antes do código

Copie [spec-template.md](../projects/spec-template.md) para `specs/<nome>.md` no
projeto. Todo requisito indispensável precisa de um critério observável; registre
também o fora de escopo.

## 3. Escolha o menor perfil

Selecione um [perfil](../profiles/README.md) e consulte
[as decisões mínimas](../catalog/stacks.md). Antes de instalar, monte a matriz:

| Necessidade | Escolha | Status/evidência | Custo/licença | Alternativa OSS | Motivo e limite |
|---|---|---|---|---|---|

- E3 pode entrar quando necessário.
- E1/E2 vira primeiro uma tarefa de validação.
- Serviço pago ou híbrido exige comparação com
  [alternativa open source](../catalog/paid-services.md).
- Referência, metodologia e prática não são pacotes para instalar.

## 4. Prepare Windows + WSL2

No PowerShell, confirme o WSL e crie ou clone o projeto sem registrar caminhos
pessoais na documentação pública:

```powershell
wsl --status
wsl --list --verbose
```

Dentro do WSL2, prefira um diretório no filesystem Linux:

```bash
git init
mkdir -p specs docs scripts
git status --short --branch
python3 --version
node --version
npm --version
```

Use um ambiente autoritativo por execução. Não compartilhe `node_modules`, ambientes
virtuais ou caches entre Windows e WSL2. Veja [toolchain](toolchain.md) e o
[playbook WSL2](../playbooks/wsl2.md).

## 5. Faça um ciclo focal

Escolha um critério e execute `SPEC → RECON → RED → BUILD → TEST → REVIEW →
CORRECT → VERIFY → CI → LEARN`. Uma tarefa pequena deve produzir código,
verificação, documentação e evidência coerentes; não acrescente dependências para
necessidades futuras.

## 6. Feche com prova

Antes de compartilhar:

- compare o resultado com cada critério;
- execute testes no estado atual;
- confirme CI remoto quando houver;
- procure segredos, PII, caminhos pessoais e dados de produção;
- registre ambiente, data e resultado essencial;
- separe provado, inferido, não verificado e bloqueado;
- informe custos, alternativas OSS e diferenças relevantes.

No próprio repositório desta base, execute `python scripts/verify_repository.py`.
Em um projeto novo, copie ou crie verificações equivalentes aos seus requisitos.
