# SCHEMA.md — Modelagem dos Dados

## Schema Prisma do MVP

```prisma
// Schema Prisma — Gerenciador de Finanças Pessoais (MVP)
// Banco de dados: SQLite

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "sqlite"
  url      = env("DATABASE_URL")
}

model Categoria {
  id          Int          @id @default(autoincrement())
  nome        String       @unique
  tipoPadrao  String?
  ativo       Boolean      @default(true)
  criadoEm   DateTime     @default(now())
  lancamentos Lancamento[]

  @@map("categorias")
}

model Lancamento {
  id             Int       @id @default(autoincrement())
  tipo           String    // 'receita' ou 'despesa'
  valor          Float
  dataLancamento DateTime
  descricao      String?
  criadoEm      DateTime  @default(now())
  atualizadoEm  DateTime? @updatedAt
  categoriaId    Int
  categoria      Categoria @relation(fields: [categoriaId], references: [id])

  @@map("lancamentos")
}
```

## Script SQL consolidado

```sql
-- Schema do Gerenciador de Finanças Pessoais (MVP)
-- SQLite

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS categorias (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        TEXT    NOT NULL UNIQUE,
    tipo_padrao TEXT    NULL
                CHECK (tipo_padrao IN ('receita', 'despesa')),
    ativo       INTEGER NOT NULL DEFAULT 1
                CHECK (ativo IN (0, 1)),
    criado_em   TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS lancamentos (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo            TEXT    NOT NULL
                    CHECK (tipo IN ('receita', 'despesa')),
    valor           NUMERIC NOT NULL CHECK (valor > 0),
    data_lancamento TEXT    NOT NULL,
    descricao       TEXT    NULL,
    categoria_id    INTEGER NOT NULL,
    criado_em       TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em   TEXT    NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Índices para agilizar consultas de filtros
CREATE INDEX IF NOT EXISTS idx_lancamentos_data
    ON lancamentos (data_lancamento);

CREATE INDEX IF NOT EXISTS idx_lancamentos_tipo
    ON lancamentos (tipo);

CREATE INDEX IF NOT EXISTS idx_lancamentos_categoria
    ON lancamentos (categoria_id);

CREATE INDEX IF NOT EXISTS idx_lancamentos_data_tipo
    ON lancamentos (data_lancamento, tipo);

-- Carga inicial de categorias (opcional, mas facilita a primeira execução)
INSERT OR IGNORE INTO categorias (nome, tipo_padrao) VALUES
    ('Salário',     'receita'),
    ('Freelance',   'receita'),
    ('Alimentação', 'despesa'),
    ('Transporte',  'despesa'),
    ('Moradia',     'despesa'),
    ('Saúde',       'despesa'),
    ('Lazer',       'despesa');
```

## Decisões de modelagem

- **Um único usuário:** não há model de usuário no MVP. O sistema assume que há apenas uma pessoa usando o aplicativo localmente.
- **Tipo como texto controlado:** o campo tipo armazena `'receita'` ou `'despesa'`. Esse controle é reforçado na camada de serviço e no SQL com CHECK.
- **Valor como Float:** no MVP, o valor monetário é armazenado como número decimal. Em evolução futura, pode migrar para inteiro de centavos.
- **Datas como DateTime/TEXT:** no SQLite, mapeado para texto no formato `YYYY-MM-DD`.

## Correspondência Prisma ↔ SQL

| Prisma | SQL |
|--------|-----|
| `model Categoria` | `CREATE TABLE categorias` |
| `model Lancamento` | `CREATE TABLE lancamentos` |
| `@id @default(autoincrement())` | `INTEGER PRIMARY KEY AUTOINCREMENT` |
| `String @unique` | `TEXT NOT NULL UNIQUE` |
| `String?` | `TEXT NULL` |
| `Boolean @default(true)` | `INTEGER NOT NULL DEFAULT 1` |
| `@relation(...)` | `FOREIGN KEY (categoria_id) REFERENCES categorias(id)` |
