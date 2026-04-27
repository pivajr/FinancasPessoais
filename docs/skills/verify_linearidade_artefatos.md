# Skill Doc — Verificar linearidade dos artefatos

## Objetivo

Garantir que a cadeia de artefatos mantém sua linearidade e coerência:

```
problema → escopo → fluxo → dados → implementação → validação → memória
```

## Passo a passo

1. Ler README.md (visão geral do projeto)
2. Ler docs/PRD.md (escopo e requisitos)
3. Ler docs/FLOW.md (comportamento do sistema)
4. Ler docs/SCHEMA.md (estrutura de dados)
5. Ler MEMORY.md (decisões e desvios)
6. Para cada requisito funcional do PRD, verificar:
   - O fluxo cobre o comportamento esperado?
   - O schema sustenta os dados necessários?
   - O código implementa o requisito?

## Checklist de linearidade

- [ ] Cada RF do PRD tem correspondência no FLOW?
- [ ] Cada entidade do SCHEMA tem origem no FLOW?
- [ ] Cada tabela SQL corresponde a um model no SCHEMA Prisma?
- [ ] Cada decisão estrutural está registrada no MEMORY?
- [ ] Os critérios de aceite do PRD podem ser verificados no sistema atual?

## Saída esperada

1. Sumário de coerência por artefato
2. Lacunas ou contradições identificadas
3. Artefatos que precisam de atualização
4. Ordem de correção recomendada

## Quando usar esta skill

- Antes de iniciar um novo incremento significativo
- Após mudanças que afetam múltiplos artefatos
- Quando houver dúvida sobre o estado atual do projeto
- Periodicamente, como manutenção preventiva
