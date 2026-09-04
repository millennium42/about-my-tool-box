# Template: entrevista de projeto

Use este documento quando uma ideia ainda não tiver contexto suficiente para virar
spec. Faça no máximo três perguntas por rodada e não repita informação já obtida.

## Rodada 1 — resultado

- Qual problema precisa ser resolvido e para quem?
- Qual resultado observável tornaria a primeira versão útil?
- O que é indispensável agora e o que pode esperar?

## Rodada 2 — contexto técnico

- Onde o projeto será desenvolvido e executado? Priorize Windows + WSL2 quando essa
  for a realidade da equipe.
- Quais sistemas precisam ser integrados e quais tecnologias são obrigatórias ou
  proibidas?
- Quem fará deploy, manutenção e resposta a falhas?

## Rodada 3 — dados, custo e risco

- Que categorias de dados entram, onde ficam e quando são excluídas?
- Existe orçamento para APIs ou serviços gerenciados? Self-hosting é aceitável?
- Há requisitos legais, de segurança, prazo ou disponibilidade?

Não solicite tokens, senhas, dados pessoais ou amostras de produção. Pergunte apenas
quais variáveis serão necessárias e como serão fornecidas com segurança.

## Saída da entrevista

Depois das respostas, produza:

1. resumo e suposições;
2. spec baseada em [spec-template.md](spec-template.md);
3. perfil de stack escolhido;
4. matriz de decisão com status/evidência, custo/licença e alternativa OSS;
5. dúvidas bloqueantes restantes;
6. plano de tarefas focais e plano de verificação.

Se nenhuma dúvida material restar, não prolongue a entrevista.
