import arrow
from aiogram import Bot, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import BotCommandScopeChat
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from bot.config import settings
from bot.controllers.game import get_active_games
from bot.database.models import User

from bot.resources.commands import special_commands
from bot.resources.keyboards import new_game_menu, game_menu
from bot.resources.enums import States
from bot.resources.responses import replies

router = Router()


@router.message(CommandStart())
async def start_message(message: types.Message, state: FSMContext) -> None:
    if message.from_user.id in settings.ADMINS:
        await message.bot.set_my_commands(special_commands, scope=BotCommandScopeChat(chat_id=message.from_user.id))
    await state.clear()
    await message.answer(text=replies.get('start_reply'))


@router.message(Command('admin'))
async def admin_command(message: types.Message, db_session: AsyncSession, state: FSMContext) -> None:
    if message.from_user.id not in settings.ADMINS:
        return
    active_games = await get_active_games(db_session)
    if not active_games:
        await message.answer(text=replies.get('no_game_admin_reply'), reply_markup=new_game_menu)
    else:
        game = active_games[-1]
        created_at = arrow.get(game.created_at)
        await message.answer(text=replies.get('current_game_stats_reply').format(game.id, created_at.humanize()),
                             reply_markup=game_menu)
