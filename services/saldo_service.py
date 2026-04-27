"""
services/saldo_service.py — Obtenção e formatação do saldo consolidado.

Responsabilidade exclusiva: recuperar o saldo via repositório e formatar
o valor monetário em reais (R$). Não acessa o banco diretamente e não
importa nada de ui/.
"""

from repositories import lancamentos_repository


def obter_saldo(conn):
    """
    Retorna o saldo consolidado de todos os lançamentos.

    Parâmetros:
        conn (sqlite3.Connection): conexão aberta com o banco.

    Retorno:
        float: saldo total (receitas - despesas). Retorna 0.0 se vazio.
    """
    return lancamentos_repository.calcular_saldo(conn)


def formatar_saldo(valor):
    """
    Formata um valor float no padrão monetário brasileiro.

    Parâmetros:
        valor (float): valor a ser formatado.

    Retorno:
        str: string no formato 'R$ 1.250,00' ou 'R$ -1.250,00' para negativos.
    """
    negativo = valor < 0
    abs_valor = abs(valor)
    formatado = f"{abs_valor:,.2f}"
    formatado = formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    if negativo:
        return f"R$ -{formatado}"
    return f"R$ {formatado}"
