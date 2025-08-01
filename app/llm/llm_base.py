from abc import ABC, abstractmethod

class LLMBase(ABC):
    """
    Abstract base class for Large Language Model (LLM) integrations.
    All LLM implementations must inherit from this class and implement the generate method.
    """
    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """
        Generate a response from the LLM given a prompt.
        :param prompt: The input prompt string
        :return: The generated response string
        """
        pass
