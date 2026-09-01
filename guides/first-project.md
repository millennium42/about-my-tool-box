# Primeiro projeto

Este é o roteiro mínimo para um projeto novo. Ele foi escrito para ser executado
por uma pessoa ou por um agente de IA.

## 1. Contexto

Registre em uma frase o problema, o usuário e o resultado esperado. Depois liste
restrições de prazo, orçamento, ambiente, dados, legislação e integrações.

## 2. Spec antes do código

Copie [projects/spec-template.md](../projects/spec-template.md) para `specs/<nome>.md`.
Cada requisito deve ter uma forma de verificação. Defina também o que está fora do
escopo; isso evita que uma sugestão vire trabalho não autorizado.

## 3. Stack mínima

Escolha um [perfil](../profiles/) e use somente o menor conjunto que satisfaz a
spec. Consulte [tools.md](../catalog/tools.md). Ferramentas em avaliação não entram
na instalação inicial.

## 4. Ambiente reproduzível

```bash
git init
mkdir -p specs scripts docs
python scripts/verify_repository.py
```

Em Windows nativo, substitua `mkdir -p` pela criação equivalente no PowerShell.
Em todos os ambientes, registre versões em `docs/ambiente.md` e mantenha segredos
fora do Git.

## 5. Construção e review

Trabalhe em uma unidade pequena por vez: escreva ou ajuste a verificação, implemente,
execute, revise contra a spec e documente a evidência. Só então avance.

## 6. Fechamento

Antes de compartilhar, confirme: requisitos atendidos, testes executados, links e
comandos reproduzíveis, riscos conhecidos, documentação atualizada e ausência de
segredos ou dados pessoais.
