from datetime import datetime

from sqlalchemy import BigInteger, func
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column

from bot.resources.enums import GameStatus


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, server_default=func.now()
    )


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None] = mapped_column(String(32))
    is_admin: Mapped[bool] = mapped_column(default=False, server_default="0")

    def __str__(self):
        username = self.username if self.username else ''
        name = self.first_name if not self.last_name else self.first_name + ' ' + self.last_name
        return (
            f"{self.__class__.__name__}(id={self.id}, telegram_id={self.telegram_id}, "
            f"name={name}, username={username})"
        )

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.id < other.id


class Record(Base):
    __tablename__ = 'records'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    # player_telegram_id: Mapped[int] = mapped_column(ForeignKey('players.telegram_id'))
    game_id: Mapped[int] = mapped_column(ForeignKey('games.id'))
    buy_in: Mapped[int | None]
    buy_out: Mapped[int | None]

    def __lt__(self, other):
        return self.buy_in < other.buy_in


class Game(Base):
    __tablename__ = 'games'

    status: Mapped[GameStatus] = mapped_column(default=GameStatus.IN_PROGRESS)
    admin_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    photo_id: Mapped[str | None]
    ended_at: Mapped[datetime | None]


class Debt(Base):
    __tablename__ = 'debts'

    session_id: Mapped[int] = mapped_column(ForeignKey('games.id'), nullable=False)
    creditor_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    debtor_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    amount: Mapped[int]
    is_paid: Mapped[bool] = mapped_column(default=False, server_default="0")
    paid_at: Mapped[datetime | None]
