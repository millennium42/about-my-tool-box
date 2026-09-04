# Perfil: documentos e relatórios

## Escolha por formato

| Formato | Candidata | Verificação indispensável |
|---|---|---|
| DOCX | python-docx | extrair estrutura e renderizar para inspeção |
| PPTX | python-pptx | renderizar slides e verificar cortes/sobreposição |
| PDF | pypdf para leitura/transformação | extrair texto, conferir páginas e renderizar |
| XLSX | XlsxWriter para geração | recalcular quando aplicável e inspecionar abas/fórmulas |

Essas bibliotecas estão E1 até serem instaladas e executadas no projeto. Para
formatos ou edições que elas não suportem, escolha outra ferramenta com o mesmo
processo de fonte, licença e evidência.

## Fluxo mínimo

1. Defina público, formato, tamanho e critérios visuais.
2. Use fonte de dados autorizada, versionada e sem PII desnecessária.
3. Gere de forma determinística.
4. Valide texto, estrutura, links, metadados e placeholders.
5. Renderize páginas ou slides e faça inspeção visual.
6. Reexecute após qualquer alteração e entregue a evidência sanitizada.

Abrir o arquivo não prova layout, acessibilidade, fórmulas ou prontidão para uso.
