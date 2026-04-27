# Gerenciador de Finanças Pessoal

Aplicação desktop local para controle financeiro individual, desenvolvida em
Python, com interface gráfica Tkinter e banco de dados SQLite.

## Objetivo

Permitir que um usuário registre receitas e despesas, visualize saldo,
consulte histórico de lançamentos e aplique filtros por período,
categoria e tipo — tudo de forma local, sem internet e sem servidor.

## Características do MVP

- Cadastro de receitas e despesas
- Categorias associadas a cada lançamento
- Data, valor e descrição opcional
- Listagem com filtros básicos (período, categoria, tipo)
- Saldo consolidado
- Persistência local em SQLite
- Execução em Windows, Linux e macOS

## Stack

- Python 3.12
- Tkinter (GUI nativa)
- SQLite (banco local, sem instalação adicional)

## Estrutura do projeto

- `main.py`              → ponto de entrada
- `database.py`          → inicialização e conexão com o banco
- `repositories/`        → acesso a dados
- `services/`            → regras de negócio
- `ui/`                  → interface gráfica
- `docs/`                → artefatos de contexto, PRD, fluxo, schema

## Como preparar o ambiente

Consulte `docs/skills/prepare_local_environment.md`.

## Como executar

```
python main.py
```

Em Linux/macOS, substitua por `python3 main.py` se necessário.

## Como construir com agentes (Claude Code / Codex)

Consulte as skill docs específicas:

- `docs/skills/build_with_claude_code.md`
- `docs/skills/build_with_codex.md`

## Artefatos importantes

Antes de modificar o sistema, leia:

- `docs/PRD.md`
- `docs/FLOW.md`
- `docs/SCHEMA.md`
- `AGENTS.md`
- `CLAUDE.md`
- `MEMORY.md`

## Filosofia do projeto

Este projeto foi intencionalmente mantido simples.
O objetivo não é demonstrar sofisticação arquitetural,
mas coerência entre problema, fluxo, modelagem e implementação.
