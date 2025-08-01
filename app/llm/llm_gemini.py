from .llm_base import LLMBase
import httpx

class GeminiLLM(LLMBase):
    """
    LLM implementation for Gemini model integration (cloud-based).
    """
    async def generate(self, prompt: str) -> str:
        """
        Generate a response using the Gemini API.
        :param prompt: The input prompt string
        :return: The generated response string
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://gemini.googleapis.com/v1/generate",
                json={"prompt": prompt},
                headers={"Authorization": "Bearer <YOUR_API_KEY>"}
            )
            response.raise_for_status()
            return response.json().get("response", "")
