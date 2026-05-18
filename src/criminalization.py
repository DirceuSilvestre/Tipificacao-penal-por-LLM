# importa bibliotecas

import json
import logging
from pathlib import Path
from datetime import datetime
import time

# importa funções de outros arquivos

from main import TIPO_DATASET
from prompt_builder import montar_prompt
from llm_client import LLMClient, LLMClientError
from utils import obter_numero_arquivo, criar_checkpoint_inicial, salvar_checkpoint, limpar_converter_texto
from config import LLM_REQUEST_DELAY_SECONDS, LLM_ARCHIVE_DELAY_SECONDS

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

                if dados_checkpoint["total_itens"] < dados_checkpoint["proximo_indice"]:
                    logger.info(f"Arquivo {caminho_arquivo.name} já processado, seguindo para o próximo...")
                    continue

                elif dados_checkpoint["total_itens"] >= dados_checkpoint["proximo_indice"]:
                    logger.info(f"Continuando processamento de {caminho_arquivo.name} do índice {dados_checkpoint['proximo_indice']}")
                   
            except Exception as e:
                logger.error(f"Erro ao abrir o checkpoint {caminho_checkpoint.name}: {e}")

        else:
            # 2. Criar checkpoint inicial
            checkpoint = criar_checkpoint_inicial(caminho_arquivo)
            salvar_checkpoint(caminho_checkpoint, checkpoint)
            logger.info(f"Checkpoint inicial criado para {caminho_arquivo.name}")

        try:
            processar_arquivo_unico(caminho_arquivo, caminho_checkpoint, client)
            # Aguardar um tempo extra entre os arquivos para evitar problemas de taxa de requisição
            time.sleep(LLM_ARCHIVE_DELAY_SECONDS)  
        except Exception as e:
            logger.error(f"Erro ao processar {caminho_arquivo}: {e}")



def processar_arquivo_unico(caminho_arquivo: Path, caminho_checkpoint: Path, client: LLMClient) -> bool:
    """
    Processa um único arquivo de condutas, realizando a tipificação por LLM.

    Args:
        caminho_arquivo: Path do arquivo a processar
        caminho_checkpoint: Path do arquivo de checkpoint
        client: Instância do cliente LLM para realizar as chamadas   
    """
    
    respostas_tipificadas = []
    id_conduta = 0

    try:
        with open(caminho_checkpoint, 'r', encoding='utf-8') as f:
            dados_checkpoint = json.load(f)

    except Exception as e:
                logger.error(f"Erro ao abrir o checkpoint {caminho_checkpoint.name}: {e}")

    numero_arquivo = obter_numero_arquivo(caminho_arquivo)

    if dados_checkpoint["proximo_indice"] == 0:
        id_conduta = ((numero_arquivo - 1) * 6) + 1
    
    else:
        id_conduta = ((numero_arquivo - 1) * 6) + dados_checkpoint["proximo_indice"]

    logger.info(f"Iniciando processamento de {dados_checkpoint["total_itens"]} casos")

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_arquivo = json.load(f)

    except Exception as e:
                logger.error(f"Erro ao abrir o checkpoint {caminho_arquivo.name}: {e}")

    while dados_checkpoint["total_itens"] <= dados_checkpoint["proximo_indice"]:

        # Encontra o tudo referente ao id desejado ou retorna None se não existir
        resultado = next((item for item in dados_arquivo if item["id"] == id_conduta), None)

        # Extrai o texto da conduta do id desejado
        conduta = resultado["texto"]

        # Monta o prompt com a conduta do id desejado
        prompt_pronto = montar_prompt(texto=conduta)

        # Envia o prompt para a função que vai chamar a LLM e receber a resposta
        resposta = client.gerar_conteudo(prompt_pronto)

        # Limpa a resposta e converte para um dicionário
        resposta_limpa = limpar_converter_texto(resposta)

        respostas_tipificadas.append(resposta_limpa)

        # Atualiza o checkpoint
        dados_checkpoint["proximo_indice"] += 1
        dados_checkpoint["timestamp_ultima_atualizacao"] = datetime.now().isoformat()

        # Atualiza id_conduta para o próximo id
        id_conduta += 1 

        salvar_checkpoint(caminho_checkpoint, dados_checkpoint)

        # Aguardar um tempo entre as requisições para evitar throttling da API
        time.sleep(LLM_REQUEST_DELAY_SECONDS)

    # salvar_respostas(respostas_tipificadas, numero_arquivo)


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