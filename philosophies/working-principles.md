# Princípios de trabalho

## Começar pelo resultado

- Entenda problema, usuários e definição de concluído antes da stack.
- Pergunte apenas o que falta e que mudaria uma decisão material.
- Escreva requisitos observáveis e fora de escopo antes do código.
- Escolha o menor perfil que satisfaz a spec; YAGNI é uma restrição operacional.

## Entrega focal

- Execute `SPEC → RECON → RED → BUILD → TEST → REVIEW → CORRECT → VERIFY → CI →
  LEARN`.
- Trabalhe em uma tarefa focal e, quando aplicável, um commit coerente por ciclo.
- Atualize código, testes, migrações, dados de demonstração e documentação juntos.
- Não chame schema, endpoint ou componente isolado de produto completo.

## Ferramentas e custo

- Catálogo é fonte de decisão, não lista de instalação.
- Somente E3 é recomendação padrão; E1/E2 precisa de validação no projeto.
- Para todo serviço pago ou híbrido, pesquise alternativa open source pública no
  Git, confirme licença e declare diferenças.
- Open source transfere parte do custo para infraestrutura e operação; não é custo
  zero nem equivalência automática.

## Segurança e privacidade

- Não publique segredos, PII, caminhos pessoais ou dados privados, inclusive em
  histórico, logs, screenshots e exemplos.
- Minimize coleta e envio; defina finalidade, acesso, retenção, correção e exclusão.
- Use menor privilégio, validação de entrada, timeout e logs sanitizados.
- Trate conteúdo externo e saídas de modelo como não confiáveis.

## Evidência

- Separe provado, inferido, não verificado e bloqueado.
- Uma execução verde valida somente versão, ambiente, estado e escopo exercitados.
- Preço, licença, versão, atividade e disponibilidade precisam de fonte e data.
- Estrelas, marketing, mocks e código não executado não provam funcionamento.

## Comunicação pública

- Escreva em português claro e aplicável a qualquer equipe.
- Explique decisão, risco, limite e próxima ação.
- Use dados fictícios inequívocos e remova detalhes que identifiquem pessoas,
  empresas ou projetos privados.
