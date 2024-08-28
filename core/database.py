# Cria um objeto de conexão (engine ) e define a classe Session

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    expire_on_commit=False,
    autoflush=False,
    bind=engine
)