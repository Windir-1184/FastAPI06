# Dependencias => Funções e objetos que outras funçoes dependem

from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def getSession():
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()

        