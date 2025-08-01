from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    """
    SQLAlchemy model for the customers table.
    """
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    address = Column(String)
    phone = Column(String)
    status = Column(String)
