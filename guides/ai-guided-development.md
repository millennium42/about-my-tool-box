# Desenvolvimento guiado por IA

Este é o fluxo canônico para transformar uma ideia em uma entrega verificável. Ele
serve para Codex, Claude Code, Cursor e outros agentes capazes de ler o repositório.

## 1. Contrato de início

O agente começa lendo `README.md`, `AGENTS.md`, a documentação local do projeto e o
perfil aplicável. Ele não instala o catálogo inteiro e não assume que uma ferramenta
citada está disponível.

Se o contexto estiver incompleto, o agente entrevista. Cada rodada deve ter no
máximo três perguntas curtas, aproveitar todas as respostas anteriores e priorizar
somente decisões que mudariam escopo, arquitetura, custo, privacidade ou aceite.

## 2. Entrevista mínima

Descubra, nesta ordem:

1. **Resultado** — qual problema será resolvido, para quem e com qual resultado.
2. **Aceite** — o que precisa ser observável para considerar a entrega concluída.
3. **Escopo** — o que é indispensável agora e o que fica explicitamente de fora.
4. **Ambiente** — Windows, WSL2, Linux ou macOS; execução local, cloud ou ambos.
5. **Dados** — categorias, origem, sensibilidade, retenção, acesso e exclusão.
6. **Restrições** — prazo, orçamento, tecnologia obrigatória/proibida e integrações.
7. **Operação** — quem fará deploy, monitoramento, atualização e resposta a falhas.

Use [o template de entrevista](../projects/interview-template.md). Não peça ao usuário
segredos reais; registre apenas nomes de variáveis e o mecanismo seguro de entrega.

## 3. Entregáveis antes do código

O agente apresenta:

- resumo do problema e suposições;
- requisitos e fora de escopo;
- critérios de aceite e como cada um será provado;
- perfil escolhido;
- matriz de ferramentas;
- riscos, dúvidas bloqueantes e plano em unidades pequenas.

A matriz é obrigatória:

| Necessidade | Escolha | Status/evidência | Custo/licença | Alternativa OSS | Motivo e diferença |
|---|---|---|---|---|---|

Para serviço pago, freemium ou híbrido, consulte
[serviços e alternativas OSS](../catalog/paid-services.md) e confirme a situação
atual na fonte pública. Uma alternativa não deve ser descrita como equivalente se
exigir self-hosting, perder recursos gerenciados ou mudar o modelo de segurança.

## 4. Gates de decisão

### Gate da spec

Não comece a implementação enquanto objetivo, requisitos indispensáveis, fora de
escopo e definição de concluído estiverem claros. Dúvida reversível pode ser
registrada como suposição; dúvida que altera dados, custo ou arquitetura exige
pergunta.

### Gate da ferramenta

- E3 permite uso padrão quando a spec realmente precisa da ferramenta.
- E1/E2 exige uma tarefa de validação: instalar em ambiente limpo, executar o caso
  mínimo, observar o resultado e registrar limites.
- Uma prática, artigo ou protocolo não entra como dependência.
- Uma fonte arquivada, ambígua ou sem licença compatível é retirada da seleção.

### Gate de privacidade

Antes do primeiro commit, classifique os dados e defina minimização, retenção,
acesso e exclusão. Antes de cada entrega, procure segredos, PII, caminhos pessoais,
logs sensíveis e exemplos copiados de produção.

### Gate de conclusão

Uma afirmação só é **provada** quando o teste cobre a afirmação no ambiente
declarado. Documentação pode sustentar uma inferência, não substituir a execução.

## 5. Ciclo focal

Para cada tarefa da spec:

1. **SPEC** — escolha um critério de aceite.
2. **RECON** — confirme código, dependências, testes e estado do Git.
3. **RED** — crie uma verificação que falha pelo motivo esperado, quando aplicável.
4. **BUILD** — implemente o menor recorte suficiente.
5. **TEST** — execute verificações automatizadas e manuais pertinentes.
6. **REVIEW** — compare diff e comportamento com requisito, risco e privacidade.
7. **CORRECT** — corrija os desvios encontrados.
8. **VERIFY** — repita os testes e registre evidência essencial.
9. **CI** — confirme a validação remota quando houver.
10. **LEARN** — atualize decisões, documentação e próxima tarefa.

Prefira uma tarefa focal e um commit coerente por ciclo. Não misture refatoração não
necessária com uma entrega funcional.

## 6. Relato final

O handoff deve dizer:

- o que ficou pronto;
- quais critérios foram provados e por quais comandos;
- ambiente e data da execução;
- o que foi apenas inferido, não verificado ou bloqueado;
- riscos e próximos passos reais;
- serviços pagos escolhidos, alternativas OSS avaliadas e motivo da decisão.

Nunca dependa de mensagens intermediárias para explicar o estado final.
