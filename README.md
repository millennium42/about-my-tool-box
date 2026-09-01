# About My Tool Box

Base de conhecimento pública, em português, para iniciar projetos de software e
IA com decisões pequenas, verificáveis e fáceis de compartilhar.

O repositório reúne princípios, metodologias, ferramentas, MCPs, perfis de stack e
playbooks generalizados. Ele não impõe uma stack e não transforma uma referência
interessante em recomendação sem instalação, uso mínimo e verificação registrados.

## Comece por aqui

Para iniciar um projeto novo, leia [o guia de primeiro projeto](guides/first-project.md)
e use o perfil mais próximo do seu caso em [profiles/](profiles/). No Codex, uma
mensagem inicial útil é:

```text
Use https://github.com/millennium42/about-my-tool-box como guia.
Leia README.md, guides/first-project.md e o perfil aplicável.
Use somente ferramentas com status Verificada; trate as demais como referência.
Antes de construir, produza a spec, as decisões de stack e os critérios de verificação.
```

O mesmo fluxo pode ser adaptado para Claude Code, Cursor e outros agentes; consulte
[a matriz de adaptação](guides/ai-agents.md).

## O que existe neste repositório

| Área | Conteúdo | Próximo arquivo |
|---|---|---|
| Princípios | YAGNI, segurança, escopo, documentação e evidência | [working-principles.md](philosophies/working-principles.md) |
| Metodologias | Spec, build, review, aprendizado e escrita humana | [methodologies/](methodologies/) |
| Catálogo | Ferramentas verificadas, em avaliação e referências | [tools.md](catalog/tools.md) |
| MCP | Conceitos, seleção, configuração e template | [mcp-servers.md](catalog/mcp-servers.md) |
| Perfis | Kits mínimos por tipo de projeto | [profiles/](profiles/) |
| Playbooks | Procedimentos granulares e generalizados | [playbooks/](playbooks/) |
| Skills | Instruções reutilizáveis para agentes | [skills/](skills/) |
| Templates | Spec, checklist e documentação de MCP | [projects/](projects/) |
| Qualidade | Checagem local, CI e atualização periódica | [verification.md](guides/verification.md) |

## Regra de status

- **Verificada**: instalação, uso mínimo e verificação foram executados e estão
  descritos. É a única categoria recomendada por padrão.
- **Em avaliação**: existe uma fonte oficial e uma hipótese de uso, mas ainda falta
  evidência completa. Não deve ser instalada automaticamente.
- **Referência**: tecnologia ou serviço útil para comparação, sem recomendação deste
  catálogo.
- **Arquivada**: mantida apenas para histórico ou porque não atende mais aos critérios.

Uma fonte oficial acessível não prova que a ferramenta é segura, adequada ou mantida.
Essas decisões precisam de evidência separada e de uma data de revisão.

## Fluxo recomendado

1. Entender objetivo, usuários, restrições e definição de concluído.
2. Copiar [a spec](projects/spec-template.md) e escrever requisitos verificáveis.
3. Escolher um [perfil mínimo](profiles/) e registrar exceções.
4. Instalar apenas ferramentas **Verificadas** necessárias.
5. Construir em unidades pequenas, com teste ou verificação antes da próxima unidade.
6. Revisar contra a spec, atualizar a documentação e registrar evidências reais.
7. Executar `python scripts/verify_repository.py` antes de abrir um pull request.

## Regras de segurança

- Nunca publique credenciais, tokens, PII, caminhos pessoais ou dados de clientes.
- Use variáveis de ambiente e arquivos locais ignorados pelo Git.
- Trate scraping, outreach, dados pessoais e integrações externas como áreas que
  exigem análise jurídica e limites explícitos.
- Não copie código de terceiros sem conferir licença e atribuição.
- Não declare que algo funciona sem execução, saída ou evidência equivalente.

Consulte [SECURITY.md](SECURITY.md) para reportar problemas no próprio catálogo.

## Atualização e verificação

O GitHub Actions verifica a estrutura e os links em cada alteração e executa uma
checagem de atualidade semanal. A automação pode apontar uma fonte indisponível ou
desatualizada, mas uma mudança de versão ou de recomendação ainda exige revisão
humana. Consulte [a política de atualização](guides/maintenance.md).

## Contribuição

Contribuições são bem-vindas por pull request. Leia [CONTRIBUTING.md](CONTRIBUTING.md),
use o template adequado e inclua a evidência da instalação, do uso mínimo e da
verificação quando solicitar que uma ferramenta seja marcada como Verificada.

## Licença

Este repositório é distribuído sob a licença [MIT](LICENSE).
