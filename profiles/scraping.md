# Perfil: scraping autorizado

## Pré-requisitos

- autorização para coletar os dados;
- análise dos termos, robots, limites e base legal aplicável;
- destino e retenção definidos;
- tratamento de erro e rate limit;
- identificação dos dados pessoais que não devem ser coletados.

## Kit mínimo

Python com HTTP nativo ou Playwright quando há interação real de navegador. Crawl4AI,
Firecrawl, Google Maps Scraper e Apify são alternativas e não dependências padrão.

## Verificação mínima

Testar uma página autorizada, respeitar o limite de requisições, registrar somente
metadados necessários, repetir sem duplicar e provar como uma pessoa pode solicitar
correção ou exclusão quando aplicável.
