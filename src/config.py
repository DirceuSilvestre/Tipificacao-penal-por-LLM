"""
Configurações da aplicação e constantes globais.

Este módulo centraliza as configurações de variáveis de ambiente,
caminhos de entrada/saída e modelos LLM utilizados no projeto.
"""

import os
from glob import glob
from pathlib import Path
from typing import Final

# ============================================================================
# Variáveis de Ambiente
# ============================================================================
GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")

# ============================================================================
# Caminhos Base
# ============================================================================
PROJECT_ROOT: Final[Path] = Path(__file__).parent.parent
DATA_DIR: Final[Path] = PROJECT_ROOT / "data"
PROCESSED_DATA_DIR: Final[Path] = DATA_DIR / "processed"
TIPIFICADOS_DATA_DIR: Final[Path] = DATA_DIR / "tipificados"
AVALIADOS_DATA_DIR: Final[Path] = DATA_DIR / "avaliados"

# ============================================================================
# Configurações LLM
# ============================================================================
LLM_MODEL: Final[str] = "gemini-3-flash-preview"
LLM_REQUEST_DELAY_SECONDS: Final[int] = 30  # Delay entre requisições para evitar throttling
LLM_ARCHIVE_DELAY_SECONDS: Final[int] = 60  # Delay entre requisições para evitar throttling


# ============================================================================
# Tipos de Dataset
# ============================================================================
DATASET_TYPES: Final[list[str]] = ["curado", "sintetico"]