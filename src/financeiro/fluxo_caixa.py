from datetime import datetime
from dateutil.relativedelta import relativedelta


def calcular_saldo_mensal(
    renda,
    contas_fixas,
    parcelas
):
    """Calcula o saldo mensal após contas fixas e parcelas."""

    total_contas = contas_fixas["valor"].sum()
    total_parcelas = parcelas["valor_parcela"].sum()

    saldo = (
    renda
    - total_contas
    - total_parcelas
    - gastos_variaveis_mensais
)

    return {
        "renda": renda,
        "contas_fixas": total_contas,
        "parcelas": total_parcelas,
        "saldo": saldo
    }


def projetar_fluxo_caixa(
    renda,
    contas_fixas,
    parcelas,
    gastos_variaveis_mensais=0,
    meses=12
):
    """Projeta o fluxo de caixa dos próximos meses."""

    total_contas = contas_fixas["valor"].sum()

    hoje = datetime.now()
    inicio = datetime(hoje.year, hoje.month, 1)

    projecao = []

    for i in range(meses):
        mes = inicio + relativedelta(months=i)

        total_parcelas = 0

        for _, parcela in parcelas.iterrows():

            proxima = datetime.strptime(
                str(parcela["proxima_parcela"]),
                "%Y-%m-%d"
            )

            primeira_parcela = datetime(
                proxima.year,
                proxima.month,
                1
            )

            ultima_parcela = (
                primeira_parcela
                + relativedelta(
                    months=int(parcela["parcelas_restantes"]) - 1
                )
            )

            if primeira_parcela <= mes <= ultima_parcela:
                total_parcelas += parcela["valor_parcela"]

        saldo = (
            renda
            - total_contas
            - total_parcelas
            - gastos_variaveis_mensais
        )

        projecao.append({
            "mes": mes.strftime("%Y-%m"),
            "renda": renda,
            "contas_fixas": total_contas,
            "parcelas": total_parcelas,
            "gastos_variaveis": gastos_variaveis_mensais,
            "saldo": saldo
        })

    return projecao

def calcular_gastos_variaveis(transacoes, contas_fixas):
    """Calcula os gastos variáveis sem duplicar contas fixas."""

    despesas = transacoes[
        transacoes["tipo"] == "saida"
    ].copy()

    nomes_contas_fixas = contas_fixas["descricao"].str.lower().str.strip()

    despesas_variaveis = despesas[
        ~despesas["descricao"].str.lower().str.strip().isin(
            nomes_contas_fixas
        )
    ]

    return despesas_variaveis["valor"].sum()


def calcular_media_gastos_variaveis(transacoes, contas_fixas):
    """Calcula a média mensal dos gastos variáveis."""

    despesas = transacoes[
        transacoes["tipo"] == "saida"
    ].copy()

    nomes_contas_fixas = contas_fixas["descricao"].str.lower().str.strip()

    despesas_variaveis = despesas[
        ~despesas["descricao"].str.lower().str.strip().isin(
            nomes_contas_fixas
        )
    ]

    if len(despesas_variaveis) == 0:
        return 0

    quantidade_meses = (
        despesas_variaveis["data"]
        .dt.to_period("M")
        .nunique()
    )

    if quantidade_meses == 0:
        return 0

    return despesas_variaveis["valor"].sum() / quantidade_meses