from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from bot.controllers.game import get_active_games
from bot.controllers.user_controllers import get_all_users
from bot.database.models import Game, User, Record
from bot.resources.keyboards import game_menu, add_players_menu, add_funds_menu, end_game_menu
from bot.resources.responses import replies

router = Router()


@router.callback_query(F.data == 'new_game')
async def new_game_button_handler(callback: types.CallbackQuery, user: User, db_session: AsyncSession) -> None:
    new_game = Game(admin_id=user.id)
    db_session.add(new_game)
    await db_session.commit()
    await callback.message.answer(text=replies.get('start_game_report').format(new_game.id),
                                  reply_markup=game_menu)
    await callback.answer()


@router.callback_query(F.data == 'add_players')
async def add_players_button_handler(callback: types.CallbackQuery) -> None:
    await callback.message.answer(text=replies.get('add_players_menu_reply'),
                                  reply_markup=add_players_menu)
    await callback.answer()


@router.callback_query(F.data == 'add_funds')
async def add_funds_button_handler(callback: types.CallbackQuery) -> None:
    await callback.message.answer(text=replies.get('add_funds_reply'),
                                  reply_markup=add_funds_menu)
    await callback.answer()


@router.callback_query(F.data == 'end_game')
async def end_game_button_handler(callback: types.CallbackQuery) -> None:
    await callback.message.answer(text=replies.get('end_game_reply'),
                                  reply_markup=end_game_menu)
    await callback.answer()


@router.callback_query(F.data == 'add_one_player')
async def add_one_player_button_handler(callback: types.CallbackQuery) -> None:
    await callback.message.answer(text=replies.get(...))
    await callback.answer()


@router.callback_query(F.data == 'add_all_players')
async def add_all_players_button_handler(callback: types.CallbackQuery, db_session: AsyncSession) -> None:
    active_games = await get_active_games(db_session)
    game = active_games[-1]
    players = await get_all_users(db_session)
    players_list = ''
    for player in players:
        record = Record(
            user_id=player.id,
            game_id=game.id,
            buy_in=1000,
        )
        db_session.add(record)
        name = '@' + player.username if player.username else player.first_name + ' ' + player.last_name
        players_list += f'{player.id}. {name}.\n'
        # personal_message = await callback.bot.send_message(chat_id=player.telegram_id, text=caption + text,
        #                                              reply_markup=add_keyboard)
    await db_session.commit()
    await callback.message.answer(text=replies.get('add_players_report').format(game.id, players_list))
    await callback.answer()


@router.callback_query(F.data == 'add_1000_to_player')
async def add_1000_to_player_button_handler(callback: types.CallbackQuery, user: User) -> None:
    await callback.message.answer(text=replies.get(...))
    await callback.answer()


@router.callback_query(F.data == 'add_1000_to_players')
async def add_1000_to_players_button_handler(callback: types.CallbackQuery) -> None:
    await callback.message.answer(text=replies.get(...))
    await callback.answer()
