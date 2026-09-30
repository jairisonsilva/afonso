import streamlit as st


from dados.carregamento import carregar_dados
from financeiro.analise import gerar_diagnostico
from financeiro.fluxo_caixa import calcular_media_gastos_variaveis
from financeiro.analise import identificar_divida_prioritaria

from ia.agente import preparar_agente
from ia.modelo import consultar_modelo

st.set_page_config(
    page_title="AFONSO",
    page_icon="💰",
    layout="wide"
)


# ==============================
# CARREGAMENTO DOS DADOS
# ==============================

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

divida_prioritaria = identificar_divida_prioritaria(
    dados["dividas"]
)


# ==============================
# INTERFACE
# ==============================

st.title("🤖 AFONSO")
st.subheader("Seu agente financeiro")

st.write(
    f"Olá, {dados['usuario']['nome']}! "
    "Veja como está sua situação financeira."
)

st.divider()


# ==============================
# VISÃO FINANCEIRA
# ==============================

st.header("📊 Visão financeira")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Renda mensal",
        f"R$ {diagnostico['renda']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col2:
    st.metric(
        "Despesas",
        f"R$ {diagnostico['total_comprometido']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col3:
    st.metric(
        "Saldo disponível",
        f"R$ {diagnostico['saldo_disponivel']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col4:
    st.metric(
        "Dívidas",
        f"R$ {diagnostico['total_dividas']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )


# ==============================
# COMPROMETIMENTO
# ==============================

st.divider()

st.header("📈 Comprometimento da renda")

st.progress(
    min(diagnostico["percentual_comprometido"] / 100, 1.0)
)

st.write(
    f"**{diagnostico['percentual_comprometido']:.2f}%** "
    "da renda está comprometida."
)


# ==============================
# DÍVIDA PRIORITÁRIA
# ==============================

st.divider()

st.header("⚠️ Dívida prioritária")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Dívida**")
    st.write(divida_prioritaria["nome"])

with col2:
    st.write("**Saldo devedor**")
    st.write(
        f"R$ {divida_prioritaria['saldo_devedor']:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

with col3:
    st.write("**Juros mensais**")
    st.write(
        f"{divida_prioritaria['taxa_juros_mensal']:.2f}%"
    )


# ==============================
# DETALHES
# ==============================

st.divider()

st.header("📋 Detalhamento")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Contas fixas**")
    st.write(
        f"R$ {diagnostico['contas_fixas']:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

with col2:
    st.write("**Parcelas mensais**")
    st.write(
        f"R$ {diagnostico['parcelas']:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

with col3:
    st.write("**Gastos variáveis**")
    st.write(
        f"R$ {diagnostico['gastos_variaveis']:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

# ==============================
# ANÁLISE DO AFONSO
# ==============================

st.divider()

st.header("🤖 Análise do AFONSO")

if st.button("Analisar minha situação financeira"):

    with st.spinner("AFONSO está analisando seus dados..."):

        mensagens = preparar_agente(
            diagnostico,
            divida_prioritaria
        )

        resposta = consultar_modelo(
            mensagens
        )

    st.write(resposta)