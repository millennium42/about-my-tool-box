# Perfil: scraping autorizado

## Gate jurídico e de dados

Antes da implementação, confirme autorização, termos aplicáveis, robots, limites,
finalidade, base legal, categorias pessoais, retenção e processo de correção/exclusão.
Não contorne autenticação, CAPTCHA ou controles de acesso.

## Escolha progressiva

1. Cliente HTTP e parser para conteúdo estático.
2. Playwright apenas quando JavaScript ou interação forem indispensáveis.
3. Crawl4AI quando extração orientada a LLM tiver ganho medido.
4. Browser Use quando a tarefa exigir decisão de agente em páginas autorizadas.
5. Serviço gerenciado apenas quando proxies, filas ou escala justificarem custo e
   envio de dados.

Firecrawl, Maxun e Crawlee são candidatas E1. Google Maps Scraper exige atenção
específica aos termos e dados pessoais. Quando o requisito for busca de locais ou
geocodificação, compare Google Maps Platform com Nominatim/OpenStreetMap sem assumir
igualdade de cobertura ou ranking. Para Apify, Firecrawl Cloud, Browser Use Cloud
ou outro plano hospedado, consulte
[alternativas OSS](../catalog/paid-services.md).

## Verificação mínima

Teste poucas páginas autorizadas, respeite rate limit, capture somente campos
necessários, trate mudança de layout e bloqueio, repita sem duplicar e prove
eliminação dos dados. Não salve HTML, cookies ou screenshots sensíveis como evidência
pública.
