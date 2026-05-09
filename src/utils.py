# import de bibliotecas


# import de constantes e funções de outros arquivos

from config import DATASET_TYPES, OUTPUT_DATA_DIR, PROCESSED_DATA_DIR

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
        raise ValueError(f"Tipo de dataset inválido: {tipo}. Esperado: {DATASET_TYPES}")
    
    padrão = str(PROCESSED_DATA_DIR / tipo / "condutas_*.json")
    caminhos_arquivos = sorted([Path(f) for f in glob(padrão)])
    
    if not caminhos_arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo de entrada encontrado para tipo '{tipo}' "
            f"no padrão: {padrão}"
        )
    
    return caminhos_arquivos


def obter_arquivos_saida(tipo: str) -> list[Path]:
    """
    Descobre automaticamente os arquivos de saída (respostas LLM) usando glob.
    
    Encontra todos os arquivos que seguem o padrão 'respostas_llm*.json'
    na pasta de saída para o tipo especificado.

    Args:
        tipo: Tipo do dataset ('curado' ou 'sintetico')

    Returns:
        Lista de Path dos arquivos encontrados, ordenada

    Raises:
        ValueError: Se o tipo de dataset não for válido
        FileNotFoundError: Se nenhum arquivo encontrado
    """
    if tipo not in DATASET_TYPES:
        raise ValueError(f"Tipo de dataset inválido: {tipo}. Esperado: {DATASET_TYPES}")
    
    padrão = str(OUTPUT_DATA_DIR / tipo / "respostas_llm*.json")
    arquivos = sorted([Path(f) for f in glob(padrão)])
    
    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo de saída encontrado para tipo '{tipo}' "
            f"no padrão: {padrão}"
        )
    
    return arquivos