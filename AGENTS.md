## Propósito do projeto

Este repositório contém o projeto Gerenciador de Finanças Pessoal:
aplicação desktop local para controle financeiro individual,
desenvolvida em Python, com interface gráfica Tkinter e banco SQLite.

## Objetivo do MVP

Permitir que um único usuário local:

- Cadastre receitas e despesas
- Associe categorias
- Registre data, valor e descrição
- Visualize saldo consolidado
- Consulte histórico
- Aplique filtros básicos por período, categoria e tipo

## Stack obrigatória do MVP

- Python 3.12
- Tkinter para GUI
- SQLite para persistência local

## Fontes de verdade do projeto

Leia nesta ordem antes de qualquer tarefa:

1. `docs/PRD.md`         → define escopo
2. `docs/FLOW.md`        → define comportamento
3. `docs/SCHEMA.md`      → define estrutura de dados
4. `MEMORY.md`           → registra decisões e exceções

Em caso de conflito entre artefatos:

- PRD prevalece sobre fluxo
- Fluxo prevalece sobre schema
- MEMORY.md registra os desvios justificados

## Restrições obrigatórias

1. Não migrar o projeto para web.
2. Não trocar Tkinter por outro framework sem instrução explícita.
3. Não introduzir múltiplos usuários no MVP.
4. Não introduzir autenticação.
5. Não criar integrações bancárias ou APIs externas.
6. Não adicionar dependências pesadas sem necessidade documentada.
7. Não acoplar SQL diretamente em widgets da GUI.
8. Não transformar o projeto em arquitetura enterprise.
9. Não alterar convenções sem registrar em MEMORY.md.

## Como atuar ao receber uma tarefa

Sempre nesta ordem:

1. Entender o pedido
2. Verificar aderência ao PRD
3. Verificar coerência com FLOW e SCHEMA
4. Identificar quais arquivos precisam mudar
5. Propor a menor mudança coerente
6. Implementar sem extrapolar o escopo
7. Explicar impacto e próximos passos

## O que verificar antes de alterar código

- A funcionalidade está no MVP?
- O fluxo já prevê esse comportamento?
- O schema atual suporta a mudança?
- Há decisão anterior registrada em MEMORY.md?
- A alteração aumenta acoplamento desnecessário?

## Política de falha explícita

Se faltar contexto relevante:

- Não improvise silenciosamente.
- Declare a lacuna com clareza.
- Proponha no máximo 2 alternativas curtas.
- Peça confirmação quando a decisão impactar escopo, fluxo ou modelagem.

## Tarefas comuns e suas skill docs

| Tarefa                          | Skill doc                                |
|----------------------------------|------------------------------------------|
| Implementar incremento           | docs/skills/implement_increment.md       |
| Verificar integridade            | docs/skills/verify_artifact_integrity.md |
| Preparar ambiente local          | docs/skills/prepare_local_environment.md |
| Executar localmente              | docs/skills/run_local_app.md             |
| Construir com Claude Code        | docs/skills/build_with_claude_code.md    |
| Construir com Codex CLI          | docs/skills/build_with_codex.md          |

## Estilo de resposta esperado

Ao responder sobre mudanças no projeto:

1. Explique brevemente o entendimento
2. Diga o que será alterado e por quê
3. Mostre o código necessário
4. Explique como executar/testar
5. Registre limitações restantes
