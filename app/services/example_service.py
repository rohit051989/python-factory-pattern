from app.schemas.example import ExampleRequest, ExampleResponse
from app.llm.llm_base import LLMBase
from app.llm.llm_factory import get_llm
from typing import Optional
import asyncio

class ExampleService:
    """
    Service layer for example operations, demonstrating LLM integration.
    """
    def __init__(self, llm: Optional[LLMBase] = None):
        """
        Initialize the service with an LLM implementation.
        :param llm: LLMBase instance (optional)
        """
        self._db = {1: {"id": 1, "name": "Sample", "value": 100}}
        self._next_id = 2
        self.llm = llm or get_llm()

    def get_example(self) -> ExampleResponse:
        """
        Get a sample example from the in-memory database.
        :return: ExampleResponse schema
        """
        data = self._db[1]
        return ExampleResponse(**data)

    async def create_example(self, request: ExampleRequest) -> ExampleResponse:
        """
        Create a new example using the LLM to process the request.
        :param request: ExampleRequest schema
        :return: ExampleResponse schema
        """
        llm_result = await self.llm.generate(request.name)
        new_id = self._next_id
        self._db[new_id] = {"id": new_id, "name": request.name, "value": request.value}
        self._next_id += 1
        # Optionally, you can store llm_result or return it
        return ExampleResponse(id=new_id, name=request.name, value=request.value)

def get_example_service():
    """
    Dependency provider for ExampleService.
    :return: ExampleService instance
    """
    return ExampleService()
