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
    """Calcula quanto da renda está comprometido."""

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
    """Calcula quanto da renda sobra."""

    total_contas_fixas = calcular_contas_fixas(contas_fixas)
    total_parcelas = calcular_parcelas_mensais(parcelas)

    saldo = renda - total_contas_fixas - total_parcelas

    return saldo


def gerar_diagnostico(
    renda,
    contas_fixas,
    parcelas,
    gastos_variaveis,
    dividas
):
    """Gera um diagnóstico financeiro consolidado."""

    total_contas_fixas = calcular_contas_fixas(contas_fixas)
    total_parcelas = calcular_parcelas_mensais(parcelas)
    total_dividas = dividas["saldo_devedor"].sum()

    total_comprometido = (
        total_contas_fixas
        + total_parcelas
        + gastos_variaveis
    )

    saldo_disponivel = renda - total_comprometido

    percentual_comprometido = (
        total_comprometido / renda
    ) * 100

    return {
        "renda": renda,
        "contas_fixas": total_contas_fixas,
        "parcelas": total_parcelas,
        "gastos_variaveis": gastos_variaveis,
        "total_comprometido": total_comprometido,
        "saldo_disponivel": saldo_disponivel,
        "percentual_comprometido": percentual_comprometido,
        "total_dividas": total_dividas
    }


def classificar_situacao(diagnostico):
    """Classifica a situação financeira."""

    percentual = diagnostico["percentual_comprometido"]
    saldo = diagnostico["saldo_disponivel"]

    if saldo < 0:
        return "deficit"

    if percentual >= 80:
        return "alto_comprometimento"

    if percentual >= 60:
        return "comprometimento_moderado"

    return "situacao_controlada"


def identificar_divida_prioritaria(dividas):
    """Identifica a dívida com maior taxa de juros."""

    indice = dividas["taxa_juros_mensal"].idxmax()

    return dividas.loc[indice]