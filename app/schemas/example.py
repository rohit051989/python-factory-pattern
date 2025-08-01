from pydantic import BaseModel

class ExampleRequest(BaseModel):
    name: str
    value: int

class ExampleResponse(BaseModel):
    id: int
    name: str
    value: int
