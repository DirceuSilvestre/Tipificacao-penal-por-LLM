"""
Cliente para comunicação com o modelo LLM (Gemini).

Este módulo fornece uma interface para interagir com a API do Google Gemini,
gerenciando autenticação, configurações de modelo e requisições de geração
de conteúdo.
"""

import logging
import google.genai as gg

from config import GEMINI_API_KEY, LLM_MODEL

logger = logging.getLogger(__name__)


class LLMClientError(Exception):
    """Exceção levantada para erros do cliente LLM."""
    pass


class GeminiClient:
    """
    Cliente para interagir com o modelo Gemini da Google.
    
    Implementa um padrão singleton para reutilizar a mesma instância
    de cliente, evitando overhead de criação repetida.
    """
    
    _instance: "GeminiClient | None" = None
    
    def __new__(cls) -> "GeminiClient":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self) -> None:
        if self._initialized:
            return
        
        if GEMINI_API_KEY is None:
            logger.error("GEMINI_API_KEY não foi definida como variável de ambiente")
            raise LLMClientError(
                "Variável de ambiente GEMINI_API_KEY não foi definida. "
                "Configure-a usando: export GEMINI_API_KEY='sua_chave' (Linux/Mac) "
                "ou set GEMINI_API_KEY=sua_chave (Windows)"
            )
        
        try:
            self.client = gg.Client(api_key=GEMINI_API_KEY)
            self._initialized = True
            logger.info(f"Cliente Gemini inicializado com sucesso usando modelo {LLM_MODEL}")
        except Exception as e:
            logger.error(f"Erro ao inicializar cliente Gemini: {e}")
            raise LLMClientError(f"Falha ao inicializar cliente Gemini: {e}")
    
    def gerar_conteudo(self, prompt: str) -> str:
        """
        Gera conteúdo usando o modelo Gemini.
        
        Args:
            prompt: Texto do prompt a ser enviado para o modelo
            
        Returns:
            Texto da resposta gerada pelo modelo
            
        Raises:
            LLMClientError: Se houver erro na geração de conteúdo
        """
        try:
            logger.debug(f"Enviando requisição para o modelo {LLM_MODEL}")
            response = self.client.models.generate_content(
                model=LLM_MODEL,
                contents=prompt
            )
            
            logger.debug("Resposta recebida com sucesso")
            return response.text
            
        except Exception as e:
            logger.error(f"Erro ao gerar conteúdo com modelo {LLM_MODEL}: {e}")
            raise LLMClientError(f"Falha ao gerar conteúdo: {e}")