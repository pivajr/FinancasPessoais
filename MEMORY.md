# MEMORY.md

## Objetivo deste arquivo

Registrar decisões, convenções, limitações conhecidas, desvios conscientes
e aprendizados do projeto. Atualizar sempre que algo estrutural mudar.

---

## Decisão 001 — Stack base do MVP

Stack definida: Python 3.12 + Tkinter + SQLite.
Justificativa: simplicidade, execução local e caráter didático.
Data: [preencher na criação]

---

## Decisão 002 — Escopo inicial controlado

MVP inclui: cadastro, categorias, data, valor, descrição,
listagem, saldo, filtros básicos.

MVP NÃO inclui: múltiplos usuários, autenticação, nuvem,
integração bancária, relatórios avançados.

---

## Decisão 003 — Arquitetura mínima

Separação obrigatória entre:

- ui/           → interface gráfica
- services/     → regras de negócio
- repositories/ → persistência SQLite

Não concentrar lógica em main.py.

---

## Decisão 004 — Convenção de data

Formato: YYYY-MM-DD (texto no SQLite).
Justificativa: facilita filtros por período e mantém consistência.

---

## Decisão 005 — Tipos válidos de lançamento

Apenas 'receita' ou 'despesa'. Controlado via CHECK no SQL
e validação na camada de serviço.

---

## Decisão 006 — Categorias pré-cadastradas

O script de inicialização do banco insere categorias padrão
via INSERT OR IGNORE (veja docs/SCHEMA.md).
O usuário pode adicionar novas categorias em evolução futura.

---

## Limitação conhecida 001

O MVP não possui edição nem exclusão de lançamentos.
Previsto como próximo incremento.

---

## Limitação conhecida 002

O saldo consolidado é global.
A relação entre saldo e filtros poderá ser revista futuramente.

---

## Dívida técnica consciente 001

Valor monetário armazenado como NUMERIC no MVP.
Evolução futura pode migrar para inteiro de centavos.
Decisão documentada em docs/SCHEMA.md.

---

## Regra de atualização

Sempre atualizar este arquivo quando:

- Uma decisão estrutural mudar
- Um novo limite importante for identificado
- Um novo padrão operacional for adotado
- Uma dívida técnica for criada ou resolvida

---

## Sessão de construção — 2026-04-27

### Arquivos criados

- requirements.txt
- .gitignore
- database.py
- repositories/__init__.py
- repositories/lancamentos_repository.py
- services/__init__.py
- services/lancamentos_service.py
- services/saldo_service.py
- ui/__init__.py
- ui/main_window.py
- main.py

### Decisões tomadas durante a implementação

1. `conn.row_factory = sqlite3.Row` adicionado em `get_connection()` para que
   os repositórios possam acessar colunas por nome sem conversão manual,
   mantendo o código legível e sem violar a separação de camadas.

2. `root.minsize(800, 540)` adicionado em `main.py` para evitar que o layout
   fique comprimido em janelas redimensionadas para tamanhos muito pequenos.

3. Coloração de linhas no Treeview implementada (receita em verde escuro,
   despesa em vermelho escuro) via `tag_configure`, conforme previsto como
   opcional e valorizado no contrato de construção.

### Desvios em relação aos artefatos

Nenhum.

### Limitações identificadas

Nenhuma além das já registradas nas Limitações conhecidas 001 e 002.

### Próximos incrementos sugeridos

- Edição de lançamentos existentes
- Exclusão de lançamentos com confirmação
- Exportação de dados em CSV
- Testes automatizados (pytest) para services e repositories
- Cadastro de novas categorias pelo usuário
