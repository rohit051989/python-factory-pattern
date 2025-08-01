from .llm_base import LLMBase
from .llm_ollama import OllamaLLM
from .llm_gemini import GeminiLLM
from config.settings import get_settings

def get_llm() -> LLMBase:
    """
    Factory function to get the appropriate LLM implementation based on configuration.
    :return: An instance of LLMBase (OllamaLLM or GeminiLLM)
    """
    settings = get_settings()
    if getattr(settings, "llm_provider", "ollama").lower() == "gemini":
        return GeminiLLM()
    return OllamaLLM()
