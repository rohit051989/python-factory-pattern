from .llm_base import LLMBase
import httpx

class OllamaLLM(LLMBase):
    """
    LLM implementation for local OLLAMA (Llama) model integration.
    """
    async def generate(self, prompt: str) -> str:
        """
        Generate a response using the local OLLAMA server.
        :param prompt: The input prompt string
        :return: The generated response string
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama2", "prompt": prompt}
            )
            response.raise_for_status()
            return response.json().get("response", "")
