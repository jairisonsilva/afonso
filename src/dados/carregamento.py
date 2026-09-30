import json
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"


def carregar_usuario():
    caminho = DATA_DIR / "usuario.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        usuario = json.load(arquivo)

    return usuario


def carregar_transacoes():
    caminho = DATA_DIR / "transacoes.csv"

    transacoes = pd.read_csv(caminho)

    transacoes["data"] = pd.to_datetime(
        transacoes["data"]
    )

    return transacoes


def carregar_contas_fixas():
    caminho = DATA_DIR / "contas_fixas.csv"

    return pd.read_csv(caminho)


def carregar_dividas():
    caminho = DATA_DIR / "dividas.csv"

    return pd.read_csv(caminho)


def carregar_parcelas():
    caminho = DATA_DIR / "parcelas.csv"

    return pd.read_csv(caminho)


def carregar_dados():
    dados = {
        "usuario": carregar_usuario(),
        "transacoes": carregar_transacoes(),
        "contas_fixas": carregar_contas_fixas(),
        "dividas": carregar_dividas(),
        "parcelas": carregar_parcelas()
    }

    return dados