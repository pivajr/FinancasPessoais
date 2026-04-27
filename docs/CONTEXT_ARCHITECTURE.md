# CONTEXT_ARCHITECTURE.md

## Arquitetura do MVP

Três camadas claramente separadas:

1. **Interface gráfica (`ui/`)**
   - Componentes Tkinter, eventos de usuário, exibição de dados.
   - NÃO deve conter SQL nem regras de negócio.

2. **Regras de negócio (`services/`)**
   - Validações, cálculos, orquestração de operações.
   - NÃO deve acessar banco diretamente.

3. **Persistência (`repositories/`)**
   - Acesso ao SQLite via sqlite3 da biblioteca padrão.
   - NÃO deve conter lógica de interface.

## Organização dos módulos

```
main.py                   → inicialização do banco + janela principal
database.py               → conexão e criação do schema
repositories/
  lancamentos_repository.py → CRUD de lançamentos
services/
  lancamentos_service.py    → validação e orquestração
  saldo_service.py          → cálculo de saldo
ui/
  main_window.py            → interface principal Tkinter
```

## Regra de ouro

GUI não fala com banco. Banco não fala com GUI.
Services fazem a mediação.
