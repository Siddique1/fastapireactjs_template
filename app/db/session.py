from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import models here so Alembic can detect them
from app.models import user

from app.config import settings

engine = create_async_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)


async def get_db():
    async with SessionLocal() as session:
        yield session
