from datetime import datetime
import logging

from sqlalchemy import Result, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import User


async def add_user_to_db(event, db_session) -> User:
    new_user = User(
        telegram_id=event.from_user.id,
        first_name=event.from_user.first_name,
        last_name=event.from_user.last_name,
        username=event.from_user.username,
    )
    db_session.add(new_user)
    await db_session.flush()
    logging.info(f"Added new user: {new_user}")
    return new_user


async def get_user_from_db(event, db_session: AsyncSession) -> User:
    query = select(User).filter(User.telegram_id == event.from_user.id)
    result: Result = await db_session.execute(query)
    user = result.scalar()
    return user


async def toggle_user_paywall_access(user_id: int, db_session: AsyncSession) -> None:
    await db_session.execute(
        update(User).filter(User.id == user_id).values(paywall_access=func.not_(User.paywall_access))
    )


async def set_user_reminders(user_id: int, reminder_freq: int, db_session: AsyncSession) -> None:
    await db_session.execute(update(User).filter(User.id == user_id).values(reminder_freq=reminder_freq))


async def update_last_reminded_at(user_id: int, timestamp: datetime, db_session: AsyncSession) -> None:
    await db_session.execute(update(User).filter(User.id == user_id).values(last_reminded_at=timestamp))


# async def check_user_reminders(bot: Bot, db_connector: DatabaseConnector):
#     while True:
#         await asyncio.sleep(10)
#         # await asyncio.sleep(Times.ONE_HOUR.value)
#         utcnow = datetime.utcnow()
#         # if utcnow.hour == Times.UTC_STARTING_MARK.value:
#         async with db_connector.session_factory() as session:
#             for user in await get_all_users_with_reminders(session):
#                 delta = utcnow - user.last_reminded_at
#                 if delta > timedelta(seconds=user.reminder_freq * 10):
#                     logging.info(f"{'=' * 10} {'reminder sended to ' + str(user)}")
#                     await bot.send_message(chat_id=user.telegram_id, text=replies["reminder_text"])
#                     await update_last_reminded_at(user_id=user.id, timestamp=utcnow, db_session=session)
#                     await session.commit()


async def get_all_users(db_session: AsyncSession) -> list[User]:
    all_players_query = select(User)
    result: Result = await db_session.execute(all_players_query)
    players = result.scalars().all()
    return [row for row in players]
