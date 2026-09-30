from dados.carregamento import carregar_dados
from financeiro.analise import gerar_diagnostico
from financeiro.fluxo_caixa import calcular_media_gastos_variaveis
from ia.agente import preparar_agente
from ia.modelo import consultar_modelo


dados = carregar_dados()

renda = dados["usuario"]["renda_mensal"]

gastos_variaveis = calcular_media_gastos_variaveis(
    dados["transacoes"],
    dados["contas_fixas"]
)

diagnostico = gerar_diagnostico(
    renda,
    dados["contas_fixas"],
    dados["parcelas"],
    gastos_variaveis,
    dados["dividas"]
)

from financeiro.analise import identificar_divida_prioritaria
divida_prioritaria = identificar_divida_prioritaria(
    dados["dividas"]
)
mensagens = preparar_agente(
    diagnostico,
    divida_prioritaria
)

resposta = consultar_modelo(mensagens)

print("===== RESPOSTA DO AFONSO =====")
print(resposta)