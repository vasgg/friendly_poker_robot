import asyncio

from sqlalchemy.ext.asyncio import AsyncEngine

from bot.database.models import Base


async def create_or_drop_db(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all, checkfirst=True)
        # await conn.run_sync(Base.metadata.drop_all)


if __name__ == "__main__":
    from bot.database.db import db

    asyncio.run(create_or_drop_db(db.engine))
