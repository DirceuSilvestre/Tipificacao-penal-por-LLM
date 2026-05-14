# importa bibliotecas

import json
import logging
from pathlib import Path

# importa funções de outros arquivos

from main import TIPO_DATASET
from llm_client import LLMClient, LLMClientError
from utils import obter_numero_arquivo, criar_checkpoint_inicial, salvar_checkpoint

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
            try:

                with open(caminho_checkpoint, 'r', encoding='utf-8') as f:
                    dados_checkpoint = json.load(f)

                if dados_checkpoint["status"] == "completo":
                    logger.info(f"Arquivo {caminho_arquivo.name} já processado, seguindo para o próximo...")
                    continue

                elif dados_checkpoint["status"] == "processando":
                    logger.info(f"Continuando processamento de {caminho_arquivo.name} do índice {dados_checkpoint['proximo_indice']}")
                   
            except Exception as e:
                logger.error(f"Erro ao verificar status do checkpoint {caminho_checkpoint.name}: {e}")

        else:
            # 2. Criar checkpoint inicial
            checkpoint = criar_checkpoint_inicial(caminho_arquivo)
            salvar_checkpoint(caminho_checkpoint, checkpoint)
            logger.info(f"Checkpoint inicial criado para {caminho_arquivo.name}")

        try:
            processar_arquivo_unico(caminho_arquivo, caminho_checkpoint, client)
        except Exception as e:
            logger.error(f"Erro ao processar {caminho_arquivo}: {e}")

def processar_arquivo_unico(caminho_arquivo: Path, caminho_checkpoint: Path, client: LLMClient) -> bool:
    """
    Processa um único arquivo de condutas, realizando a tipificação por LLM.

    Args:
        caminho_arquivo: Path do arquivo a processar
        caminho_checkpoint: Path do arquivo de checkpoint
        client: Instância do cliente LLM para realizar as chamadas"""
    """
    o que eu preciso aqui é ler o arquivo de condutas
    ler o arquivo de checkpoint
    verifica o itens processados
    se for zero entao preenche o total de itens
    e coloca o proximo indice como o primeiro indice
    se nao for zero entao verifica o status do chekpoint so pra ter certeza que o codigo anterior nao errou
    porque se o status estiver como completo entao algo errado no codigo anterior e deve avisar

    verifica o proximo indice e usa como id da conduta que vai ser tipificada
    chama a funcao montar prompt passando a conduta como parametro
    recebe o prompt
    chama a funcao que vai tipificar a conduta que esta no prompt que deve ser passado
    recebe a resposta e coloca essa resposta em uma lista
    contabiliza nos itens processados
    quando os itens processados forem iguais ao total de itens
    entao deve salvar em um arquivo todas as respostas das condutas tipificadas em um arquivo na pasta correta
    """