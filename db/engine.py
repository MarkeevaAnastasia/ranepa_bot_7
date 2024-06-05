__all__ = [
  'async_session_maker',
  'async_create_table',
]

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlalchemy.orm import sessionmaker
from .models import Base

engine: AsyncEngine = create_async_engine (url = 'sqlite + aiosqlite:///instance/sqlite.db', echo = True)
async_session_maker: AsyncSession = async_sessionmaker(engine, class = AsyncSession, expire_on_commit = False)

#костыль переписать под AsyncEngine

async def async_create_table():
  async with engine_begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

