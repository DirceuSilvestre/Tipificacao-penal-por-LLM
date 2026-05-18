"""
Construtor de prompts para classificação penal.

Este módulo é responsável por construir prompts estruturados que orientam
o modelo LLM na classificação de condutas de acordo com a legislação penal
brasileira (crimes contra a administração pública).
"""

from typing import Final

# ============================================================================
# Definições de Classes Penais
# ============================================================================

CLASSES_PENAIS: Final[list[str]] = [
    "peculato",
    "peculato_culposo",
    "peculato_mediante_erro_de_outrem",
    "concussao",
    "corrupcao_passiva",
    "prevaricacao",
    "condescendencia_criminosa",
    "advocacia_administrativa",
    "violacao_de_sigilo_funcional",
    "nao_se_enquadra"
]

# Template do prompt com placeholders
PROMPT_TEMPLATE: Final[str] = """Você é um especialista em Direito Penal brasileiro, com foco em crimes contra a Administração Pública.

Sua tarefa é analisar a conduta descrita abaixo e classificá-la segundo as possíveis classes.

Classes possíveis:
- peculato
- peculato_culposo
- peculato_mediante_erro_de_outrem
- concussao
- corrupcao_passiva
- prevaricacao
- condescendencia_criminosa
- advocacia_administrativa
- violacao_de_sigilo_funcional
- nao_se_enquadra

Responda desta forma:
{{
"classe": "...",
"justificativa": "..."
}}

Conduta:
{texto}
"""


def montar_prompt(texto: str) -> str:
    """
    Constrói um prompt para classificação de conduta penal.

    Esta função prepara um prompt estruturado contendo instruções para
    o modelo LLM classificar uma conduta de acordo com as classes penais
    definidas no projeto.

    Args:
        texto: Descrição da conduta a ser classificada

    Returns:
        Prompt formatado pronto para envio ao modelo LLM

    Raises:
        ValueError: Se o texto estiver vazio ou None
    """
    if not texto or not isinstance(texto, str):
        raise ValueError("Texto da conduta deve ser uma string não-vazia")
    
    texto = texto.strip()
    
    return PROMPT_TEMPLATE.format(texto=texto)