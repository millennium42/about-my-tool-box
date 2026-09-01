# Princípios de trabalho

Princípios operacionais para projetos de software, dados e IA.

## YAGNI e simplicidade

- Faça o menor trabalho que resolve o requisito real.
- Prefira biblioteca padrão e recursos nativos antes de dependências.
- Não adicione uma feature porque ela talvez seja útil depois.
- Registre a exceção quando uma dependência adicional for necessária.

## Qualidade e entrega

- Escreva critérios de aceite verificáveis antes da implementação.
- Use teste antes da correção quando houver regressão reproduzível.
- Trabalhe em recortes pequenos e faça review contra a spec.
- Atualize código, testes, migrações, seeds e documentação que mudarem juntos.
- Diferencie recorte técnico encerrado de integração ou produto ainda pendente.

## Segurança e privacidade

- Não publique segredos, PII ou dados inventados.
- Não use mocks em produção.
- Não edite uma migration já aplicada; crie uma migration aditiva.
- Use menor privilégio, timeout, validação de entrada e logs sem dados sensíveis.
- Para dados pessoais, defina finalidade, retenção, acesso, exclusão e base legal.

## Evidência

- Não declare funcionamento sem execução, estado ou saída observável.
- Separe provado, inferido, não verificado e bloqueado.
- Uma execução verde valida apenas o escopo e o estado exercitados.
- Preços, estoque, versões, popularidade e notícias precisam de data de consulta.

## Comunicação

- Escreva em português claro, direto e natural.
- Explique a decisão, o risco e a próxima ação.
- Não prometa resultado que não possa ser entregue.
- Em outreach, respeite recusa e mantenha um opt-out claro.
