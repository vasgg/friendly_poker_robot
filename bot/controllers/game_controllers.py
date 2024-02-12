from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import Record


async def add_thousand_to_player(user_id: int, game_id: int, db_session: AsyncSession):
    record = db_session.query(Record).filter(Record.game_id == game_id, Record.player_telegram_id == telegram_id).scalar()
    add_1000 = (update(Record)
                .where(Record.game_id == game_id, Record.player_telegram_id == telegram_id)
                .values(buy_in=int(record.buy_in) + 1000))
    session.execute(add_1000)
    session.commit()
    session.close()


async def add_1000_to_player(game_id: int, player_id: int, db_session: AsyncSession): -> None:
    query = update(Record).filter(Record.game_id == game_id, Record.player_id == player_id).values(status=new_status)
    await db_session.execute(query)