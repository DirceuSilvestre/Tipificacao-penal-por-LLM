# import de bibliotecas
import json
import logging
from glob import glob
from pathlib import Path
from datetime import datetime

# import de constantes e funções de outros arquivos
from config import DATASET_TYPES, PROCESSED_DATA_DIR

def obter_caminhos_arquivos_entrada(tipo: str) -> list[Path]:
    """
    Descobre automaticamente os arquivos de entrada usando glob.
    
    Encontra todos os arquivos que seguem o padrão 'condutas_*.json'
    na pasta de dados processados para o tipo especificado.

    Args:
        tipo: Tipo do dataset ('curado' ou 'sintetico')

    Returns:
        Lista de Path dos arquivos encontrados, ordenada

    Raises:
        ValueError: Se o tipo de dataset não for válido
        FileNotFoundError: Se nenhum arquivo encontrado
    """
    if tipo not in DATASET_TYPES:
        msg_erro = f"Tipo de dataset inválido: {tipo}. Esperado: {DATASET_TYPES}"
        logging.error(msg_erro) 
        raise ValueError(msg_erro)
    
    padrão = str(PROCESSED_DATA_DIR / tipo / "condutas_*.json")
    caminhos_arquivos = sorted([Path(f) for f in glob(padrão)])
    
    if not caminhos_arquivos:
        msg_erro = f"Nenhum arquivo de entrada encontrado para tipo '{tipo}' no padrão: {padrão}"
        logging.error(msg_erro) 
        raise FileNotFoundError(msg_erro)
    
    return caminhos_arquivos

def obter_numero_arquivo(caminho_arquivo: Path) -> str:
    """
    Extrai o número do arquivo condutas_X.json
    
    Exemplo:
        condutas_5.json → "5"
        condutas_123.json → "123"
    """
    nome = caminho_arquivo.stem  # Remove a extensão
    numero = nome.replace("condutas_", "")  # Remove o prefixo
    return numero

def criar_checkpoint_inicial(caminho_arquivo: Path):
    """
    Cria um checkpoint inicial para o arquivo a ser processado.

    Args:
        caminho_arquivo: Path do arquivo para o qual criar o checkpoint

    Returns:
        Dicionário representando o checkpoint inicial
    """
    checkpoint = {
        "arquivo_referente": caminho_arquivo.name,
        "status": "processando",
        "timestamp_inicio": datetime.now().isoformat(),
        "timestamp_ultima_atualizacao": datetime.now().isoformat(),
        "total_itens": 0,
        "itens_processados": 0,
        "proximo_indice": 0,
        "erros_encontrados": []
    }

def salvar_checkpoint(caminho_checkpoint: Path, checkpoint: dict):
    """
    Salva o checkpoint em um arquivo JSON.

    Args:
        caminho_checkpoint: Path onde o checkpoint deve ser salvo
        checkpoint: Dicionário do checkpoint a ser salvo
    """
    
    with open(caminho_checkpoint, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False, indent=4)