# Humanizer — Tom Humano em Comunicação Automatizada

Técnica/ferramenta para deixar copy, mensagens e textos gerados por IA com tom
humano, sem jeito de robô. Base: https://github.com/blader/humanizer
("Agent skill that removes signs of AI-generated writing..." — ⭐ 37k+).

## Quando usar
- Qualquer texto que vá para humano real: e-mails de outreach, mensagens WhatsApp,
  UX copy, respostas de suporte, posts.
- Sempre que o texto "cheirar a IA" (lista de bullets genéricos, adjetivos vazios,
  frases passivas, "como uma IA").

## Como funciona (determinístico, não LLM)
Aplicar transformações de substituição + estrutura:
1. **Substituir jargão** por linguagem cotidiana.
   Ex.: "poderíamos oferecer" → "acho que combinaria"; "nossos serviços" →
   "o que a gente faz — sites, sistemas, automação"; "implementar" → "colocar pra rodar".
2. **Quebrar parágrafos longos** em frases curtas com pausas naturais.
3. **Remover robótica**: sem "como uma IA", sem encher de adjetivos, sem bullets vazios.
4. **Personalizar a saudação** por nome/contexto (nunca genérico).
5. **Fechar com leveza**: pergunta aberta ou "valeu", não "atenciosamente".

## Template de abordagem B2B (reutilizável)
```
Olá {nome}! Me chamo {seu_nome}, sou {seu_papel} da {empresa} ({site}).

Hoje trabalhamos com {o que vocês fazem resumido}.

Estamos com uma campanha para {contexto do lead}, oferecendo {proposta curta}.
Além da {entrega principal}, {diferencial: manutenção/consultoria}.

Gostaria de agendar uma conversa para {objetivo}?

Desde já agradeço!
```
Regra LGPD/compliance: incluir frase de opt-out ("Se não fizer sentido, me avisa
que eu não te chamo novamente."). Respeitar recusa = bloqueio permanente.

## Pitfalls de copy
- Não prometer resultado que não se entrega ("aumente vendas em X%").
- Não inventar depoimentos/números (ver `philosophies/working-principles.md` → regra 3).
- Tom direto, útil, SEM robótico.
