from fastapi import APIRouter, HTTPException, Depends
from app.schemas.example import ExampleRequest, ExampleResponse

from app.services.example_service import ExampleService, get_example_service
from app.services.customer_service import CustomerService
from app.db import get_db
from app.schemas.customer import CustomerRead
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi import status, Depends


router = APIRouter(prefix="/example", tags=["Example"])

"""
Router for example and customer endpoints.
Includes endpoints for LLM integration and customer queries.
"""



@router.get("/", response_model=ExampleResponse)
def get_example(service: ExampleService = Depends(get_example_service)):
    """
    Get a sample example object.
    """
    return service.get_example()

# New: Get all customers

@router.get("/customers", response_model=List[CustomerRead])
async def get_customers(db: AsyncSession = Depends(get_db)):
    """
    Get all customers from the database.
    """
    service = CustomerService(db)
    return await service.get_customers()

# Get customer by email

@router.get("/customers/by-email/{email}", response_model=CustomerRead)
async def get_customer_by_email(email: str, db: AsyncSession = Depends(get_db)):
    """
    Get a customer by email address.
    """
    service = CustomerService(db)
    customer = await service.get_customer_by_email(email)
    if not customer:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.post("/", response_model=ExampleResponse, status_code=status.HTTP_201_CREATED)
async def create_example(request: ExampleRequest, service: ExampleService = Depends(get_example_service)):
    """
    Create a new example using the LLM integration.
    """
    return await service.create_example(request)
