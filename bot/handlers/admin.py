from aiogram import types, Router
from aiogram.dispatcher.filters import Command

from config import dp
from bot.controllers import get_current_game, get_current_game_stats_for_admin
from db.database import session
from bot.database.models import User
from bot.resources.keyboards import current_game_admin_keyboard, new_game_menu
from resourсes.replies import answer

admin_router = Router()


@admin_router.message_handler(Command('admin'))
async def admin_command(message: types.Message):
    player = session.query(User).filter(User.telegram_id == message.from_user.id).scalar()
    if player.is_admin:
        keyboard = (
            current_game_admin_keyboard
            if await get_current_game()
            else new_game_menu
        )
        text = (
            await get_current_game_stats_for_admin()
            if await get_current_game()
            else answer['no_game_admin_reply']
        )
        await dp.bot.send_message(chat_id=message.from_user.id, text=text, reply_markup=keyboard)
    else:
        await dp.bot.send_message(chat_id=message.from_user.id, text=answer['not_admin_reply'])
