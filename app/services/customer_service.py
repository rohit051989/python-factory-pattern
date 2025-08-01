
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.customer import CustomerRead
from typing import List
from app.repositories.customer_repository import CustomerRepository

class CustomerService:
    """
    Service layer for customer-related business logic.
    Delegates data access to the CustomerRepository.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the service with a database session.
        :param db: AsyncSession instance
        """
        self.repo = CustomerRepository(db)

    async def get_customers(self) -> List[CustomerRead]:
        """
        Get all customers as Pydantic models.
        :return: List of CustomerRead schemas
        """
        customers = await self.repo.get_all()
        return [CustomerRead.model_validate(c) for c in customers]

    async def get_customer_by_email(self, email: str) -> CustomerRead | None:
        """
        Get a customer by email as a Pydantic model.
        :param email: Customer's email address
        :return: CustomerRead schema or None if not found
        """
        customer = await self.repo.get_by_email(email)
        if customer:
            return CustomerRead.model_validate(customer)
        return None
