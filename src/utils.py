# import de bibliotecas
import logging
from glob import glob
from pathlib import Path

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