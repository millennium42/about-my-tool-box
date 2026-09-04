# Verificação e níveis de evidência

## Níveis

| Nível | O que existe | Status permitido |
|---|---|---|
| E0 | Nome, hipótese ou fonte ambígua | Retirada ou pendente |
| E1 | Fonte oficial exata, licença/modelo e data consultados | Em avaliação ou Referência |
| E2 | Instalação e caso mínimo documentados, ainda sem execução suficiente | Em avaliação |
| E3 | Instalação, uso e resultado executados e reproduzíveis em ambiente registrado | Verificada |

**Somente E3** pode receber o status **Verificada**. E3 não é permanente nem
universal: ele cobre versão, ambiente, data e comportamento exercitados.

## Registro mínimo de E3

Uma evidência deve informar:

1. necessidade e afirmação que está sendo testada;
2. fonte e versão ou commit;
3. sistema operacional, runtime e pré-requisitos;
4. comando de instalação executado;
5. entrada mínima sem dados sensíveis;
6. comando ou interação executada;
7. resultado esperado e resultado observado;
8. falhas, permissões, custo e limites;
9. data e escopo da conclusão.

Para SaaS, API ou integração externa, documentação e mock não bastam. E3 exige uma
operação real autorizada ou um ambiente oficial de teste, além de timeout, erro,
política de dados e custo observados. Sem credencial ou orçamento, classifique como
**bloqueada**, não como aprovada.

## Classes para o relato

| Classe | Base | Linguagem correta |
|---|---|---|
| Provado | Teste executado que cobre a afirmação | “Executado em …; resultado …” |
| Inferido | Fonte adequada, sem execução completa | “A documentação indica …” |
| Não verificado | Ainda não investigado ou testado | “Permanece pendente” |
| Bloqueado | Falta ambiente, permissão, credencial ou decisão | “Não foi possível provar porque …” |

Não use estrelas, texto promocional, página acessível, build isolado, mock ou código
gerado como prova de funcionamento integrado.

## Verificação deste repositório

```bash
python scripts/verify_repository.py
python scripts/verify_repository.py --network
python scripts/catalog_freshness.py
```

O primeiro comando valida estrutura, links internos, contrato do catálogo,
alternativas OSS e padrões de dados sensíveis. `--network` consulta links externos,
mas disponibilidade HTTP ainda é apenas sinal de manutenção. O relatório de fontes
consulta estado, licença e atividade pública dos repositórios Git.

A evidência executada da base está em
[catalog/evidence/base-toolchain.md](../catalog/evidence/base-toolchain.md). Ela não
transforma as ferramentas E1 em E3.

## Gate de privacidade

Antes do commit e depois de gerar relatórios:

- procure segredos literais, chaves privadas e cabeçalhos de autorização;
- procure e-mails pessoais, telefones, endereços e caminhos de usuário;
- revise fixtures, screenshots, PDFs, artefatos e histórico Git;
- use somente dados fictícios inequívocos;
- se um segredo foi publicado, revogue-o e limpe o histórico. A varredura automática
  reduz risco, mas não substitui revisão humana nem um scanner especializado.
