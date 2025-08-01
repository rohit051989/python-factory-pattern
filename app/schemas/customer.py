from pydantic import BaseModel

class CustomerBase(BaseModel):
    """
    Base schema for customer data (shared attributes).
    """
    name: str
    email: str
    address: str | None = None
    phone: str | None = None
    status: str | None = None

class CustomerCreate(CustomerBase):
    """
    Schema for creating a new customer.
    """
    pass

class CustomerRead(CustomerBase):
    """
    Schema for reading customer data, including the ID.
    """
    id: int
