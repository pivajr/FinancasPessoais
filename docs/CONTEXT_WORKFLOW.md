# CONTEXT_WORKFLOW.md

## Fluxo humano-agente recomendado

1. Ler README.md
2. Ler docs/PRD.md
3. Ler docs/FLOW.md
4. Ler docs/SCHEMA.md
5. Ler AGENTS.md
6. Ler CLAUDE.md
7. Verificar MEMORY.md
8. Consultar a skill doc apropriada
9. Iniciar a codificação

## Antes de codificar — perguntas obrigatórias

- Esta tarefa está dentro do MVP?
- Esta mudança altera o fluxo?
- Esta mudança exige alteração no schema?
- Esta decisão precisa ser registrada em MEMORY.md?

## Depois de codificar — verificações

- Os artefatos ainda estão coerentes?
- O sistema funciona localmente?
- README e MEMORY precisam ser atualizados?

## Para profissionais de outras áreas

Se você não é desenvolvedor, siga este caminho simplificado:

1. Leia README.md (visão geral)
2. Leia docs/skills/build_with_claude_code.md OU
   docs/skills/build_with_codex.md
3. Siga as instruções passo a passo
4. Use o agente como parceiro de construção
5. Valide o resultado seguindo docs/skills/run_local_app.md
