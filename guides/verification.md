# Verificação

## O que precisa ser provado

Uma ferramenta é **Verificada** somente quando há:

1. fonte oficial acessível;
2. pré-requisitos declarados;
3. instalação executada em pelo menos um ambiente suportado;
4. uso mínimo executado;
5. saída ou estado observável;
6. data, ambiente e limitações registrados.

O script deste repositório verifica a documentação e os links locais. Ele não
substitui a execução da ferramenta.

```bash
python scripts/verify_repository.py
python scripts/verify_repository.py --network
```

## Níveis de evidência

| Nível | Significado |
|---|---|
| E0 | Nome ou hipótese, sem fonte suficiente |
| E1 | Fonte oficial encontrada |
| E2 | Instalação e uso mínimo documentados |
| E3 | Instalação, uso e resultado executados e reproduzíveis |

Somente E3 pode receber status **Verificada**. E1 e E2 permanecem **Em avaliação**.

## Evidência desta revisão

No ambiente de revisão, foram executados com sucesso `git --version`,
`python --version`, um script Python, `node --version`, `npm --version`, um script
Node, `docker --version`, `docker compose version` e `docker info`. A verificação
do repositório encontrou 40 arquivos Markdown, 48 links internos e 71 links
externos válidos em 2026-09-01.

Essa evidência cobre o kit de base e a documentação. Não significa que todas as
ferramentas externas da tabela estejam instaladas.

## O que não é prova

Quantidade de estrelas, texto promocional, uma página que abre, código gerado,
estimativa de desempenho e relato sem comando reproduzível não substituem E3.
