# importa bibliotecas

import logging

# importa funções de outros arquivos

from pathlib import Path
from main import TIPO_DATASET
from llm_client import LLMClient, LLMClientError
from utils import obter_numero_arquivo

logger = logging.getLogger(__name__)

def processar_arquivos(caminhos_arquivos: list[Path]):
    """
    Processa todos os arquivos de condutas a partir do ultimo arquivo processado.

    Args:
        caminhos_arquivos: Lista de Path dos arquivos a processar
    """

    client = LLMClient()

    for caminho_arquivo in caminhos_arquivos:
        
        numero = obter_numero_arquivo(caminho_arquivo)
        caminho_checkpoint = caminho_arquivo.parent / f"checkpoint_{numero}.json"

        # verificar se o arquivo de checkpoint existe na pasta onde esta o arquivo que sera processado
        # se sim, pular o processamento do arquivo e passar para o próximo, 
        # se não, criar o checkpoint inicial e iniciar o processamento do arquivo

        if caminho_checkpoint.exists():

            if caminho_checkpoint["status"] == "completo":
                logger.info(f"Arquivo {caminho_arquivo.name} já processado, seguindo para o próximo...")
                continue

            elif caminho_checkpoint["status"] == "processando":
                logger.info(f"Continuando processamento de {caminho_arquivo.name} do índice {caminho_checkpoint['proximo_indice']}")
                # Passa o checkpoint para processar_arquivo_unico

        else:
            # 2. Criar checkpoint inicial
            checkpoint = criar_checkpoint_inicial(caminho_arquivo)
            salvar_checkpoint(checkpoint_path, checkpoint)
            logger.info(f"Checkpoint inicial criado para {caminho_arquivo.name}")

        try:
            processar_arquivo_unico(caminho_arquivo, client)
        except Exception as e:
            logger.error(f"Erro ao processar {caminho_arquivo}: {e}")

def processar_arquivo_unico(caminho_arquivo: Path, client: LLMClient) -> bool:
    """
    Processa um único arquivo de condutas, realizando a tipificação por LLM.

    Args:
        caminho_arquivo: Path do arquivo a processar
        client: Instância do cliente LLM para realizar as chamadas"""