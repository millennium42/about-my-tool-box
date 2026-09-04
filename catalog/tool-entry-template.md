# Modelo de entrada de ferramenta

Copie esta estrutura para documentar uma candidata. Não use dados reais em exemplos
ou saídas.

```markdown
## Nome exato

- **Necessidade**: problema concreto que resolve
- **Tipo**: CLI, runtime, biblioteca, MCP, skill ou serviço
- **Status/evidência**: Em avaliação / E1
- **Repositório ou fonte oficial exata**: URL
- **Versão ou commit avaliado**: valor + data
- **Licença/modelo de custo**: licença e plano aplicável
- **Atividade**: público? arquivado? último release/push observado em AAAA-MM-DD
- **Compatibilidade**: Windows, WSL2, Linux, macOS
- **Pré-requisitos e permissões**: runtime, rede, arquivos e dados
- **Instalação**: comando reproduzível
- **Uso mínimo**: comando ou prompt reproduzível
- **Verificação**: resultado esperado e observado
- **Segurança e privacidade**: dados enviados, retenção, logs e exclusão
- **Riscos/limites**: lock-in, operação, manutenção e falhas conhecidas
- **Última validação**: AAAA-MM-DD, ambiente e versão

## Serviço pago, freemium ou híbrido

- **Alternativa OSS pública no Git**: URL do repositório
- **Licença confirmada em**: AAAA-MM-DD
- **Diferença funcional/operacional**: sem alegar equivalência indevida
```

Só altere o status para **Verificada** quando a evidência for E3 conforme
[guides/verification.md](../guides/verification.md). Se o nome, fonte ou licença não
puder ser resolvido, registre em [retired.md](retired.md), não na seleção ativa.
