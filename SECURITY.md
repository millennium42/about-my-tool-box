# Segurança e privacidade

Não publique em issue, pull request, commit ou artefato:

- credencial, token, cookie, chave privada ou cabeçalho de autorização;
- nome, e-mail, telefone, endereço ou outro dado pessoal desnecessário;
- caminho de usuário, hostname, IP interno ou URL privada;
- dado de cliente, amostra de produção ou instrução que permita acesso indevido.

Relate vulnerabilidades e exposições pelo mecanismo privado de segurança do GitHub.
Não inclua o valor completo de um segredo; informe apenas tipo, local, intervalo de
commits e impacto suficiente para reprodução segura.

## Se um segredo entrar no Git

1. Revogue ou rotacione o segredo imediatamente na origem.
2. Interrompa automações que ainda o utilizem.
3. Remova o valor do estado atual e do histórico alcançável.
4. Force a atualização apenas com autorização e coordene clones/forks.
5. Confirme refs, tags, artefatos, caches e logs; peça remoção ao provedor quando
   necessário.
6. Registre apenas a correção sanitizada.

Reescrever histórico reduz exposição, mas não torna seguro um segredo já publicado.

## Ferramentas externas

Um link não é endosso de segurança, disponibilidade ou licença. Antes de instalar,
revise código, permissões, dependências, dados enviados e manutenção. MCPs e agentes
devem receber a menor capacidade possível.

O verificador local detecta alguns padrões comuns, não todos. Use também revisão
humana e o scanner de segredos adotado pelo projeto.
