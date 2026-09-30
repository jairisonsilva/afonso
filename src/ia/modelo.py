from ollama import chat


def consultar_modelo(mensagens, modelo="qwen3:1.7b"):
    """Envia as mensagens para o modelo e retorna a resposta."""

    resposta = chat(
        model=modelo,
        messages=mensagens
    )

    return resposta.message.content