
Pipeline real, testado end-to-end, que gera leads com WhatsApp **confirmado**
para oferecer sites/sistemas a pequenos negócios de Santa Maria/RS.

## Arquitetura
```
Google Maps Scraper (Docker gosom, :8081)
   POST /api/v1/jobs {query: "restaurante santa maria"}
   → polling até done
   → GET /api/v1/jobs/{id}/download  (CSV: nome, phone, site, categoria, endereço, lat/lon)
        ↓
Filtro Hermes:
   - sem site próprio (website vazio no Maps)
   - + (celular PJ OU perfil social)
   - NÃO franquia (decisão centralizada → -50 score)
        ↓
Crawl4AI (Docker unclecode/crawl4ai, :11235, Bearer hermes_crawl_super_secret_2026)
   POST /crawl {urls: [perfis Instagram/Facebook]}
   procura: wa.me / api.whatsapp / agrupadores (linktr.ee, beacons, bio.link)
        ↓
Hermes qualifica (ranqueia por probabilidade de compra)
CrewAI MCP ranqueia + redige abordagem WhatsApp
        ↓
        ↓
Dispara WhatsApp APENAS em número confirmado (wa.me no perfil Instagram)
```

## Resultado real obtido
- 13 jobs → 127 empresas únicas de Santa Maria.
- Filtro: 42 elegíveis (sem site + contato).
- 28 com WhatsApp confirmado salvos no Google Contacts (prefixo `[Code House]`).

## Scoring usado
- +30: empresa sem site
- +30: empresa sem software visível
- +20: rating ≥ 4.0 mas sem site
- -50: franquia

## Pitfalls (não repetir)
1. **Imagem Crawl4AI errada** → `unclecode/crawl4ai:latest`. `crawl4ai/crawl4ai` dá
   *pull access denied*.
2. **Endpoint** → `/crawl` recebe `urls` (lista), não `url`. `markdown` vem como
   **dict** (json.dumps antes de regex).
3. **IPv6 trap** → usar `127.0.0.1:11235` (localhost trava em `::1`).
4. **Scraper 404** em query genérica ("empresa santa maria") → usar categoria
   específica (restaurante, pet shop, mecânica).
5. **Crawl4AI lento** (~15–20s/Instagram) → rodar em background, não execute_code 5min.
6. **execute_code bufferiza print** → `flush=True` + salvar JSON a cada etapa.

## Verificação honesta de WhatsApp
- `wa.me/<num>` e `api.whatsapp.com/send?phone=` NÃO distinguem número inexistente
  de existente (ambos 200/302 com número falso).
- Google Maps e Facebook NÃO expõem wa.me no HTML (bloqueiam bot).
- Única confirmação automática confiável: `wa.me` presente no PRÓPRIO perfil Instagram.
- Demais leads = "alta probabilidade (celular PJ)" → verificação manual de 2s.

## Mensagem de oferta (template, corpo idêntico, saudação por nome)
```
Olá {nome}! Me chamo Pablo, sou sócio fundador da Code House (pablo-codehouse.surge.sh).

Hoje trabalhamos com soluções personalizadas para o ambiente comercial, corporativo ou industrial.

Estamos com uma campanha para a digitalização de negócios locais de Santa Maria, oferecendo
um valor abaixo do mercado para a criação do Site Institucional do seu negócio. Além da
construção, oferecemos consultoria para hospedagem e mantemos a manutenção do site por 1 ano.

Gostaria de agendar uma reunião online ou presencial para conversarmos melhor?

Desde já agradeço!
```
