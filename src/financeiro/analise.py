def calcular_contas_fixas(contas_fixas):
    """Calcula o total das contas fixas mensais."""
    return contas_fixas["valor"].sum()


def calcular_parcelas_mensais(parcelas):
    """Calcula o total das parcelas mensais."""
    return parcelas["valor_parcela"].sum()


def calcular_gastos_variaveis(transacoes):
    """Calcula o total de gastos variáveis."""
    gastos = transacoes[transacoes["tipo"] == "saida"]

    return gastos["valor"].sum()


def calcular_comprometimento_renda(
    renda,
    contas_fixas,
    parcelas
):
    """Calcula quanto da renda está comprometido com despesas fixas e parcelas."""

    total_contas_fixas = calcular_contas_fixas(contas_fixas)
    total_parcelas = calcular_parcelas_mensais(parcelas)

    total_comprometido = total_contas_fixas + total_parcelas

    percentual = (total_comprometido / renda) * 100

    return {
        "contas_fixas": total_contas_fixas,
        "parcelas": total_parcelas,
        "total_comprometido": total_comprometido,
        "percentual_comprometido": percentual
    }


def calcular_saldo_disponivel(
    renda,
    contas_fixas,
    parcelas
):
    """Calcula quanto da renda sobra após contas fixas e parcelas."""

    total_contas_fixas = calcular_contas_fixas(contas_fixas)
    total_parcelas = calcular_parcelas_mensais(parcelas)

    saldo = renda - total_contas_fixas - total_parcelas

    return saldo
