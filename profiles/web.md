# Perfil: aplicações web

## Árvore de decisão

| Necessidade | Início mínimo | Só adicione quando |
|---|---|---|
| Página estática | HTML, CSS e JavaScript | Vite para build ou módulos |
| SPA interativa | Vite + TypeScript | React quando componentes/estado justificarem |
| SSR ou full-stack TypeScript | Next.js + TypeScript | PostgreSQL para persistência relacional |
| Backend/admin PHP | Laravel + PostgreSQL | Filament/Livewire para backoffice |
| Cache/fila | Nenhum inicialmente | Valkey quando carga ou job assíncrono for medido |

Autenticação deve usar solução mantida e compatível com o framework. Antes de
adotar Better Auth ou provedor hospedado, modele sessão, recuperação, autorização,
MFA, retenção e exclusão.

## Gate de validação

As bibliotecas web estão E1 no catálogo. Para promovê-las no projeto: crie aplicação
mínima, fixe dependências, execute build/teste, abra rota de saúde, exercite erro e
registre versões no Windows/WSL2 escolhido.

## Deploy

Compare serviço gerenciado com Coolify ou outra opção OSS atual. Registre custo,
domínio/TLS, preview, banco, backup, observabilidade e rollback; self-hosting não é
equivalente automático.

## Conclusão mínima

Teste fluxo principal, migração descartável, autenticação/autorização aplicável,
acessibilidade básica, segredo fora do bundle, build de produção e CI no commit.
