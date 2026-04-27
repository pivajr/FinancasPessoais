"""
repositories/lancamentos_repository.py — Acesso a dados via SQLite.

Responsabilidade exclusiva: executar SQL para leitura e escrita das tabelas
categorias e lancamentos. Não contém lógica de negócio, validações nem
referências a ui/ ou services/.

Todas as funções recebem conn (sqlite3.Connection) como primeiro parâmetro.
"""


def listar_categorias(conn):
    """
    Retorna todas as categorias ativas.

    Parâmetros:
        conn (sqlite3.Connection): conexão aberta com o banco.

    Retorno:
        list[dict]: lista de dicionários com chaves 'id', 'nome', 'tipo_padrao'.
    """
    cursor = conn.execute(
        "SELECT id, nome, tipo_padrao FROM categorias WHERE ativo = 1 ORDER BY nome"
    )
    return [dict(row) for row in cursor.fetchall()]


def inserir_lancamento(conn, tipo, valor, data_lancamento, categoria_id, descricao=None):
    """
    Insere um novo lançamento no banco.

    Parâmetros:
        conn (sqlite3.Connection): conexão aberta com o banco.
        tipo (str): 'receita' ou 'despesa'.
        valor (float): valor monetário maior que zero.
        data_lancamento (str): data no formato YYYY-MM-DD.
        categoria_id (int): id da categoria associada.
        descricao (str | None): descrição opcional do lançamento.

    Retorno:
        int: id do registro inserido (lastrowid).
    """
    cursor = conn.execute(
        """
        INSERT INTO lancamentos (tipo, valor, data_lancamento, categoria_id, descricao)
        VALUES (?, ?, ?, ?, ?)
        """,
        (tipo, valor, data_lancamento, categoria_id, descricao),
    )
    conn.commit()
    return cursor.lastrowid


def listar_lancamentos(conn, tipo=None, categoria_id=None, data_inicio=None, data_fim=None):
    """
    Retorna lançamentos com filtros opcionais.

    Parâmetros:
        conn (sqlite3.Connection): conexão aberta com o banco.
        tipo (str | None): 'receita' ou 'despesa'; None = sem filtro.
        categoria_id (int | None): id da categoria; None = sem filtro.
        data_inicio (str | None): data mínima no formato YYYY-MM-DD; None = sem filtro.
        data_fim (str | None): data máxima no formato YYYY-MM-DD; None = sem filtro.

    Retorno:
        list[dict]: lista de dicionários com chaves 'id', 'tipo', 'valor',
                    'data_lancamento', 'descricao', 'categoria_id',
                    'nome_categoria', 'criado_em'.
    """
    sql = """
        SELECT
            l.id,
            l.tipo,
            l.valor,
            l.data_lancamento,
            l.descricao,
            l.categoria_id,
            c.nome AS nome_categoria,
            l.criado_em
        FROM lancamentos l
        JOIN categorias c ON c.id = l.categoria_id
        WHERE 1=1
    """
    parametros = []

    if tipo is not None:
        sql += " AND l.tipo = ?"
        parametros.append(tipo)

    if categoria_id is not None:
        sql += " AND l.categoria_id = ?"
        parametros.append(categoria_id)

    if data_inicio is not None:
        sql += " AND l.data_lancamento >= ?"
        parametros.append(data_inicio)

    if data_fim is not None:
        sql += " AND l.data_lancamento <= ?"
        parametros.append(data_fim)

    sql += " ORDER BY l.data_lancamento DESC, l.id DESC"

    cursor = conn.execute(sql, parametros)
    return [dict(row) for row in cursor.fetchall()]


def calcular_saldo(conn):
    """
    Calcula o saldo consolidado: soma das receitas menos soma das despesas.

    Parâmetros:
        conn (sqlite3.Connection): conexão aberta com o banco.

    Retorno:
        float: saldo total. Retorna 0.0 se não houver lançamentos.
    """
    cursor = conn.execute(
        """
        SELECT
            COALESCE(SUM(CASE WHEN tipo = 'receita' THEN valor ELSE 0 END), 0.0)
            - COALESCE(SUM(CASE WHEN tipo = 'despesa' THEN valor ELSE 0 END), 0.0)
            AS saldo
        FROM lancamentos
        """
    )
    row = cursor.fetchone()
    return float(row["saldo"]) if row and row["saldo"] is not None else 0.0
