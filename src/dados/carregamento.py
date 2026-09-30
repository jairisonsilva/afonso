import json
from pathlib import Path

import pandas as pd


# Caminho da pasta raiz do projeto
ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"


def carregar_usuario():
    """Carrega os dados do usuário a partir do arquivo JSON."""
    caminho = DATA_DIR / "usuario.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        usuario = json.load(arquivo)

    return usuario


def carregar_transacoes():
    """Carrega as transações financeiras."""
    caminho = DATA_DIR / "transacoes.csv"

    return pd.read_csv(caminho)


def carregar_contas_fixas():
    """Carrega as contas fixas."""
    caminho = DATA_DIR / "contas_fixas.csv"

    return pd.read_csv(caminho)


def carregar_dividas():
    """Carrega as dívidas."""
    caminho = DATA_DIR / "dividas.csv"

    return pd.read_csv(caminho)


def carregar_parcelas():
    """Carrega as parcelas."""
    caminho = DATA_DIR / "parcelas.csv"

    return pd.read_csv(caminho)


def carregar_dados():
    """
    Carrega todos os dados financeiros do usuário
    e retorna um dicionário com as informações.
    """

    dados = {
        "usuario": carregar_usuario(),
        "transacoes": carregar_transacoes(),
        "contas_fixas": carregar_contas_fixas(),
        "dividas": carregar_dividas(),
        "parcelas": carregar_parcelas()
    }

    return dados
