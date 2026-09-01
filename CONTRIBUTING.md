# Contribuindo

Obrigado por ajudar a manter esta base pública, pequena e confiável.

## Antes de abrir um pull request

1. Explique o problema ou a lacuna que a mudança resolve.
2. Prefira uma mudança pequena e uma ferramenta por vez.
3. Não inclua credenciais, PII, caminhos pessoais, nomes de clientes ou conteúdo
   específico de projetos privados.
4. Para uma ferramenta nova, use o modelo de [entrada de ferramenta](catalog/tool-entry-template.md)
   e indique a fonte oficial.
5. Se usar o status **Verificada**, registre instalação, uso mínimo, saída observada,
   data e ambiente.
6. Rode `python scripts/verify_repository.py`.

## Critérios para uma ferramenta verificada

- fonte oficial acessível;
- instalação reproduzível para pelo menos um ambiente suportado;
- exemplo mínimo executado;
- verificação observável e repetível;
- limites, custo, permissões e riscos documentados;
- nenhuma afirmação de versão ou popularidade sem data e fonte.

## Revisão

O pull request deve responder: o que mudou, por que é útil, como foi verificado e
qual parte ainda depende de validação manual. Mudanças de status, segurança e
compatibilidade recebem atenção especial.
