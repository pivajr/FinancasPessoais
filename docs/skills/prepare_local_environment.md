# Skill Doc — Preparar ambiente local

## Objetivo

Orientar a preparação do ambiente para desenvolvimento e execução local
em Windows, Linux e macOS.

## Pré-requisitos

- Python 3.12 instalado
- Terminal disponível
- Permissões de leitura/escrita na pasta do projeto

## Verificar instalação do Python

```bash
python --version
# ou
python3 --version
# Esperado: Python 3.12.x
```

## Windows

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Verificar disponibilidade de Tkinter

```bash
python -c 'import tkinter; tkinter._test()'
# Uma janela de teste deve abrir
```

## Verificar disponibilidade de sqlite3

```bash
python -c 'import sqlite3; print(sqlite3.version)'
```

## Política de falha

Se Tkinter não estiver disponível:

- Linux (Ubuntu/Debian): `sudo apt-get install python3-tk`
- macOS: reinstalar Python via python.org (versão com Tk incluso)
- Windows: reinstalar Python marcando a opção tcl/tk
