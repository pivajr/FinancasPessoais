"""
database.py — Conexão e inicialização do banco de dados SQLite.

Responsabilidade exclusiva: abrir conexão com o banco e criar o schema
(tabelas, índices e categorias padrão) caso ainda não existam.

Não importa nada de ui/, services/ ou repositories/.
"""

import sqlite3


def get_connection(db_path="financas.db"):
    """
    Abre e retorna uma conexão SQLite com chaves estrangeiras ativas.

    Parâmetros:
        db_path (str): caminho para o arquivo do banco. Padrão: 'financas.db'.

    Retorno:
        sqlite3.Connection: conexão aberta, pronta para uso.
    """
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db(db_path="financas.db"):
    """
    Cria as tabelas, índices e categorias padrão se ainda não existirem.

    Parâmetros:
        db_path (str): caminho para o arquivo do banco. Padrão: 'financas.db'.

    Retorno:
        None
    """
    conn = get_connection(db_path)

    conn.executescript("""
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

        CREATE INDEX IF NOT EXISTS idx_lancamentos_data
            ON lancamentos (data_lancamento);

        CREATE INDEX IF NOT EXISTS idx_lancamentos_tipo
            ON lancamentos (tipo);

        CREATE INDEX IF NOT EXISTS idx_lancamentos_categoria
            ON lancamentos (categoria_id);

        CREATE INDEX IF NOT EXISTS idx_lancamentos_data_tipo
            ON lancamentos (data_lancamento, tipo);

        INSERT OR IGNORE INTO categorias (nome, tipo_padrao) VALUES
            ('Salário',     'receita'),
            ('Freelance',   'receita'),
            ('Alimentação', 'despesa'),
            ('Transporte',  'despesa'),
            ('Moradia',     'despesa'),
            ('Saúde',       'despesa'),
            ('Lazer',       'despesa');
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_db()
    print("Banco inicializado com sucesso: financas.db")
