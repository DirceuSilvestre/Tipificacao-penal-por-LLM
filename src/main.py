"""
Script principal para tipificação penal por LLM.

Este módulo executa o pipeline completo de classificação de condutas:
1. Verifica quantos arquivos tem em uma pasta para serem processados
Para cada arquivo:
    1. Carrega dados dos arquivos processados
    2. Processa casos através do modelo LLM
    3. Salva resultados em arquivos de saída

Configuração:
    Configure a variável de ambiente GEMINI_API_KEY antes de executar:
    
    Windows (CMD):
        set GEMINI_API_KEY=sua_chave_aqui
        python src/main.py
    
    Windows (PowerShell):
        $env:GEMINI_API_KEY="sua_chave_aqui"
        python src/main.py
    
    Linux/Mac:
        export GEMINI_API_KEY=sua_chave_aqui
        python src/main.py
"""

# importar as funcoes de outros arquivos

import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("tipificacao_penal.log")
    ]
)
logger = logging.getLogger(__name__)