from ia.prompts import SYSTEM_PROMPT, criar_prompt
from financeiro.resumo import gerar_fatos_financeiros


def preparar_agente(diagnostico, divida_prioritaria):
    """Prepara as mensagens que serão enviadas ao modelo de IA."""

    fatos = gerar_fatos_financeiros(
        diagnostico,
        divida_prioritaria
    )

    mensagem_usuario = criar_prompt(fatos)

    mensagens = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": mensagem_usuario
        }
    ]

    return mensagens