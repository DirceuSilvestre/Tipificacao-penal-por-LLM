"""
Script principal para tipificação penal por LLM.

Este módulo executa o pipeline completo de classificação de condutas:
1. Verifica quantos arquivos tem em uma pasta para serem processados
Para cada arquivo:
    1. Carrega dados dos arquivos processados
    2. Processa casos através do modelo LLM
    3. Salva resultados em arquivos de saída

 - A função vai buscar na pasta de dados processados do tipo de dataset escolhido (curado ou sintetico) 
    os arquivos que seguem o padrão 'condutas_*.json' e vai retornar o caminho de cada arquivo de forma ordenada
 - a função vai conectar com a LLM
 - a função vai receber a lista de caminhos dos arquivos e para cada cada caminho:
    - a função vai ler os dados do arquivo atual
    - a função vai montar o prompt para cada caso do arquivo atual
    - a função vai enviar o prompt para a LLM e receber a resposta
    - a função vai montar a resposta com a conduta tipificada unindo a conduta e sua classe real 
        com a classe predita e sua justificativa
    - a função vai esperar 30 segundos entre as respostas para evitar throttling da LLM
    - a função vai unir as respostas do arquivo atual em uma lista e salvar em um arquivo de saída 
        seguindo o padrão 'respostas_llmX.json' onde X é o número do arquivo de entrada processado
    - a função vai exibir uma mensagem de progresso indicando qual arquivo teve suas condutas tipificadas 
        e quantos arquivos faltam para processar
    - a função vai aguardar 60 segundos entre o processamento de cada arquivo para evitar throttling da LLM


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

# import de bibliotecas

import logging
import sys
from typing import Final

# import das funções de outros arquivos

from utils import obter_caminhos_arquivos_entrada

# Configuração de Logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding='utf-8',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/tipificacao_penal.log")
    ]
)
logger = logging.getLogger(__name__)

# constante

TIPO_DATASET: Final[str] = "sintetico"  # Alterar para "sintetico" ou "curado" conforme necessário

# pipeline

def main():

    try:
        logger.info(f"Iniciando a tipificação de condutas do dataset: {TIPO_DATASET}")

        logger.debug("Obtendo caminhos dos arquivos de entrada...")
        caminhos_arquivos = obter_caminhos_arquivos_entrada(TIPO_DATASET)

    except Exception as e:
        # Captura qualquer outro erro (banco de dados, memória, etc.)
        logger.critical(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)

    "ja sabemos que esta retornando corretamente os caminhos dos arquivos de entrada"
    "agora precisamos fazer o processamento de tipificação para cada caminho de arquivo contido na variavel caminhos_arquivos"

    """
    primeiro de tudo faz a conexão com a LLM (se der erro avisa, trata e sai do programa)
    Para cada caminho de arquivo, verificar se há o checkpoint de processamento
    se existe e status completo, então pula o processamento e passa para o próximo arquivo
    se existe e processando entao continua a partir do proximo_indice
    se não houver o checkpoint, então cria, preenche com as informações
    """

    """
        CONTINUACAO DA PROGRAMACAO:
        continuar a programação da funcao processar_arquivo_unico utilizando o conteudo do checkpoint dentro da lógica para controlar cada tipificacao de cada conduta do arquivo que esta sendo processado
        fazer a programação do salvamento das condutas tipificadas do arquivo que acabou de ser processado em um arquivo de saída seguindo o padrão 'respostas_llmX.json' onde X é o número do arquivo de entrada processado e modificar o status do checkpoint para completo
    """


    logger.info("Se esta mensagem esta sendo exibida então o código funcionou corretamente!")

if __name__ == "__main__":
    main()