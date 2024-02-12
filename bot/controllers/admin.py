from sqlalchemy import update

from db.database import session
from bot.database.models import User


async def promote_to_admin(player_id: int) -> None:
    new_admin = update(User).where(User.id == player_id).values(is_admin=True)
    session.execute(new_admin)
    session.commit()
    session.close()


async def demote_from_admin(player_id: int) -> None:
    demote = update(User).where(User.id == player_id).values(is_admin=False)
    session.execute(demote)
    session.commit()
    session.close()
