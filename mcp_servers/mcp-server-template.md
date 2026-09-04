# Template: documentar um servidor MCP

Copie esta estrutura para um arquivo específico do servidor:

```markdown
# Nome do servidor

- **Status**: Em avaliação
- **Fonte oficial**: link
- **Versão validada**: versão e data
- **Ambiente**: Windows, WSL2, Linux ou macOS
- **Licença/modelo de custo**: licença, plano e limites

## O que faz

Resumo curto e limites.

## Pré-requisitos

- runtime e versão;
- dependências;
- permissões e secrets necessários.

## Instalação

Comando oficial reproduzível.

## Registro no cliente

Use o mecanismo oficial do cliente. Não altere manualmente um arquivo protegido.

## Uso mínimo

Prompt ou chamada reproduzível.

## Verificação

Comando, saída observada e data.

## Segurança e limites

Dados enviados, hosts, diretórios, operações, timeout e custo.

## Alternativa open source

Obrigatória quando o servidor ou serviço subjacente for pago, freemium ou híbrido:
repositório Git público, licença, data e diferença funcional.
```

Não coloque tokens, caminhos pessoais ou respostas sensíveis no exemplo.
