from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.customer import Customer
from typing import List

class CustomerRepository:
    """
    Repository for Customer database operations.
    Handles all queries related to the Customer table.
    """
    def __init__(self, db: AsyncSession):
        """
        Initialize the repository with a database session.
        :param db: AsyncSession instance
        """
        self.db = db

    async def get_all(self) -> List[Customer]:
        """
        Retrieve all customers from the database.
        :return: List of Customer objects
        """
        result = await self.db.execute(select(Customer))
        return list(result.scalars().all())

    async def get_by_email(self, email: str) -> Customer | None:
        """
        Retrieve a customer by email address.
        :param email: Customer's email address
        :return: Customer object or None if not found
        """
        result = await self.db.execute(select(Customer).where(Customer.email == email))
        return result.scalars().first()
