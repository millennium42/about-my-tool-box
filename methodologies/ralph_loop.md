# Loop de entrega

Adaptação pública do padrão de ciclos curtos exemplificado por
[snarktank/ralph](https://github.com/snarktank/ralph). Esta página descreve uma
metodologia; não instala nem valida o projeto de referência.

## Ciclo

1. **SPEC** — fixe requisito e aceite.
2. **RECON** — confirme o estado atual.
3. **RED** — produza a falha esperada quando aplicável.
4. **BUILD** — implemente o menor recorte.
5. **TEST** — execute a verificação.
6. **REVIEW/CORRECT** — compare com spec, risco e privacidade; corrija.
7. **VERIFY/CI** — repita localmente e confirme o commit remoto.
8. **LEARN** — documente decisões e próxima tarefa.

Faça uma tarefa focal e um commit coerente por ciclo. Um aprendizado reutilizável
pode virar playbook ou skill, desde que seja anonimizado e não copie contexto
privado.
