def gerar_fatos_financeiros(diagnostico, divida_prioritaria):
    """Gera fatos objetivos para serem apresentados pela IA."""

    fatos = f"""
DADOS FINANCEIROS:

Renda mensal: R$ {diagnostico['renda']:.2f}

Contas fixas mensais: R$ {diagnostico['contas_fixas']:.2f}

Parcelas mensais: R$ {diagnostico['parcelas']:.2f}

Gastos variáveis mensais: R$ {diagnostico['gastos_variaveis']:.2f}

Total das despesas cadastradas: R$ {diagnostico['total_comprometido']:.2f}

Saldo disponível após as despesas cadastradas: R$ {diagnostico['saldo_disponivel']:.2f}

Comprometimento da renda: {diagnostico['percentual_comprometido']:.2f}%

Saldo total das dívidas: R$ {diagnostico['total_dividas']:.2f}


DÍVIDA PRIORITÁRIA:

Nome: {divida_prioritaria['nome']}

Tipo: {divida_prioritaria['tipo']}

Saldo devedor: R$ {divida_prioritaria['saldo_devedor']:.2f}

Taxa de juros mensal: {divida_prioritaria['taxa_juros_mensal']:.2f}%


INTERPRETAÇÕES DEFINIDAS PELO SISTEMA:

- A dívida prioritária foi selecionada porque possui a maior taxa
de juros mensal entre as dívidas cadastradas.

- O saldo devedor da dívida prioritária não é uma parcela mensal.

- O saldo disponível já considera as despesas cadastradas,
incluindo as parcelas mensais.

- O sistema não calculou um valor de pagamento adicional.

- O sistema não calculou uma estratégia para quitar as dívidas.

- O sistema não determinou quanto do saldo disponível deve ser
destinado ao pagamento de uma dívida.

- O sistema não determinou redução de nenhuma categoria de despesa.

- Não foram calculadas recomendações de novos empréstimos ou crédito.
"""

    return fatos