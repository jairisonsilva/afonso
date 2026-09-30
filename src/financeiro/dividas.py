def calcular_total_dividas(dividas):
    """Calcula o total do saldo devedor atual."""
    return dividas["saldo_devedor"].sum()


def calcular_dividas_por_tipo(dividas):
    """Agrupa o saldo devedor por tipo de dívida."""
    return (
        dividas
        .groupby("tipo")["saldo_devedor"]
        .sum()
        .sort_values(ascending=False)
    )


def encontrar_maior_juros(dividas):
    """Identifica a dívida com maior taxa de juros mensal."""
    indice = dividas["taxa_juros_mensal"].idxmax()
    return dividas.loc[indice]


def contar_dividas(dividas):
    """Conta a quantidade de dívidas cadastradas."""
    return len(dividas)