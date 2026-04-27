"""
services/lancamentos_service.py — Regras de negócio para lançamentos.

Responsabilidade exclusiva: validar os dados de um lançamento e orquestrar
seu registro chamando o repositório. Não acessa o banco diretamente e não
importa nada de ui/.
"""

import datetime

from repositories import lancamentos_repository


def validar_lancamento(tipo, valor, data_lancamento, categoria_id):
    """
    Valida os campos obrigatórios de um lançamento antes de persistir.

    Parâmetros:
        tipo (str): deve ser exatamente 'receita' ou 'despesa'.
        valor: deve ser conversível para float e maior que zero.
        data_lancamento (str): deve estar no formato YYYY-MM-DD e ser data válida.
        categoria_id: deve ser inteiro maior que zero.

    Retorno:
        tuple[bool, str | None]:
            (True, None) se todos os campos são válidos.
            (False, mensagem) se algum campo é inválido.
    """
    if tipo not in ("receita", "despesa"):
        return False, "Tipo inválido. Selecione 'Receita' ou 'Despesa'."

    try:
        valor_float = float(valor)
    except (TypeError, ValueError):
        return False, "Valor inválido. Informe um número maior que zero."

    if valor_float <= 0:
        return False, "Valor deve ser maior que zero."

    try:
        datetime.date.fromisoformat(str(data_lancamento))
    except (TypeError, ValueError):
        return False, "Data inválida. Use o formato YYYY-MM-DD."

    try:
        categoria_id_int = int(categoria_id)
    except (TypeError, ValueError):
        return False, "Categoria inválida. Selecione uma categoria da lista."

    if categoria_id_int <= 0:
        return False, "Categoria inválida. Selecione uma categoria da lista."

    return True, None


def registrar_lancamento(conn, tipo, valor, data_lancamento, categoria_id, descricao=None):
    """
    Valida e persiste um novo lançamento.

    Parâmetros:
        conn (sqlite3.Connection): conexão aberta com o banco.
        tipo (str): 'receita' ou 'despesa'.
        valor: valor monetário maior que zero.
        data_lancamento (str): data no formato YYYY-MM-DD.
        categoria_id: id da categoria associada.
        descricao (str | None): descrição opcional.

    Retorno:
        int: id do lançamento inserido.

    Exceções:
        ValueError: se algum campo não passar na validação.
    """
    valido, mensagem = validar_lancamento(tipo, valor, data_lancamento, categoria_id)
    if not valido:
        raise ValueError(mensagem)

    return lancamentos_repository.inserir_lancamento(
        conn,
        tipo,
        float(valor),
        str(data_lancamento),
        int(categoria_id),
        descricao if descricao and descricao.strip() else None,
    )
