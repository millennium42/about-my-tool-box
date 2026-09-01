# Manutenção

## Automação

- Em cada pull request: validar Markdown essencial, links internos e formato do
  catálogo.
- Semanalmente: verificar fontes externas e produzir um relatório de atualidade.
- Trimestralmente: revisar instalação, uso mínimo, segurança, licença e status das
  ferramentas verificadas.

A automação pode detectar alteração; ela não deve atualizar uma recomendação de
forma cega. Uma mudança de versão, licença, preço ou comportamento exige revisão.

## Revalidar uma ferramenta

1. Abrir a fonte oficial e confirmar que ela ainda é a fonte correta.
2. Repetir a instalação em um ambiente limpo.
3. Repetir o exemplo mínimo.
4. Registrar data, versão, sistema, saída e limitações.
5. Atualizar a linha em `catalog/tools.md`.

Se a fonte desaparecer, o comando deixar de funcionar ou a licença mudar, rebaixar
o status imediatamente para **Em avaliação** ou **Arquivada**.
