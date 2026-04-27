# Skill Doc — Verificar integridade dos artefatos

## Objetivo

Verificar se PRD, FLOW, SCHEMA, MEMORY e código
continuam coerentes entre si.

## Passo a passo

1. Ler docs/PRD.md
2. Ler docs/FLOW.md
3. Ler docs/SCHEMA.md
4. Ler MEMORY.md
5. Identificar a funcionalidade em questão
6. Verificar:
   - Escopo existe no PRD?
   - Comportamento existe no FLOW?
   - Schema suporta a funcionalidade?
   - Decisão relevante em MEMORY.md?
7. Comparar com o código atual

## Saída esperada

1. Artefatos analisados
2. Pontos coerentes
3. Inconsistências encontradas
4. Ajustes prioritários

## Política de falha

Se algum artefato estiver ausente, declarar que a
verificação ficou parcial antes de concluir.
