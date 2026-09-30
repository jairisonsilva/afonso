def calcular_total_parcelas_mensais(parcelas):
    """Calcula o total das parcelas que serão pagas por mês."""
    return parcelas["valor_parcela"].sum()


def calcular_total_parcelas_restantes(parcelas):
    """Calcula a quantidade total de parcelas que ainda faltam."""
    return parcelas["parcelas_restantes"].sum()


def calcular_valor_total_restante(parcelas):
    """Calcula o valor total das parcelas restantes."""
    return (
        parcelas["valor_parcela"] *
        parcelas["parcelas_restantes"]
    ).sum()


def encontrar_maior_parcela(parcelas):
    """Identifica a maior parcela mensal."""
    indice = parcelas["valor_parcela"].idxmax()
    return parcelas.loc[indice]