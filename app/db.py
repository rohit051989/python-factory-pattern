from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from config.settings import get_settings

settings = get_settings()
DATABASE_URL = settings.database_url

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    """
    Dependency that provides a SQLAlchemy async session.
    Yields:
        AsyncSession: SQLAlchemy async session
    """
    async with AsyncSessionLocal() as session:
        yield session
