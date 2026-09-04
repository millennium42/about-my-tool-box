# Template: spec de projeto ou feature

Copie para `specs/<nome>.md` e preencha antes de construir. Use somente dados
fictícios; nunca cole credenciais, PII ou conteúdo de produção.

```markdown
# Nome do projeto ou feature

## Objetivo e usuários
- Problema:
- Usuários:
- Resultado esperado:

## Requisitos indispensáveis
- [ ] Requisito observável 1
- [ ] Requisito observável 2

## Fora de escopo
- Item que não será feito nesta iteração.

## Definição de concluído
| Critério | Como provar | Evidência esperada |
|---|---|---|
| Critério 1 | teste/comando/inspeção | saída sem dados sensíveis |

## Ambiente e operação
- Desenvolvimento: Windows / WSL2 / Linux / macOS
- Execução: local / cloud / ambos
- Deploy e rollback:
- Responsável por operação:

## Dados e privacidade
- Categorias e origem:
- Dados pessoais ou sensíveis:
- Finalidade e base aplicável:
- Armazenamento e acesso:
- Retenção, correção e exclusão:
- Dados enviados a IA, SaaS, MCP ou telemetria:

## Restrições
- Prazo:
- Orçamento:
- Tecnologia obrigatória ou proibida:
- Segurança, legislação e integrações:

## Decisões de stack
| Necessidade | Escolha | Status/evidência | Custo/licença | Alternativa OSS | Motivo e limite |
|---|---|---|---|---|---|

## Segredos necessários
- Nome da variável, finalidade e mecanismo seguro de entrega; nunca o valor.

## Riscos, suposições e pendências
| Item | Classe | Impacto | Mitigação ou pergunta |
|---|---|---|---|

## Plano de entrega
- [ ] Tarefa focal 1
- [ ] Tarefa focal 2

## Plano de verificação
- [ ] testes automatizados
- [ ] verificação manual
- [ ] integração externa real ou bloqueio declarado
- [ ] segurança, privacidade e varredura de segredos
- [ ] evidência visual, acessibilidade ou performance, se aplicável
- [ ] CI e instruções de reprodução
```

Mantenha no projeto o estado, as decisões, os comandos e as evidências. Não copie
essas informações para este repositório público se revelarem contexto privado.
