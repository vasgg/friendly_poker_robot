from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

new_game_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='new game', callback_data='new_game'),
    ],
    [
        InlineKeyboardButton(text='statistics', callback_data='statistics'),
    ]
]
)

game_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='add players', callback_data='add_players'),
    ],
    [
        InlineKeyboardButton(text='add funds', callback_data='add_funds'),
    ],
    [
        InlineKeyboardButton(text='end game', callback_data='end_game'),
    ],
]
)

add_players_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='add one player', callback_data='add_one_player'),
    ],
    [
        InlineKeyboardButton(text='add all players', callback_data='add_all_players'),
    ]
]
)

add_funds_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='add 1000 to player', callback_data='add_1000_to_player'),
    ],
    [
        InlineKeyboardButton(text='add 1000 to all players', callback_data='add_1000_to_players'),
    ]
]
)

add_funds_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='add 1000', callback_data='self add 1000'),
            InlineKeyboardButton(text='exit game', callback_data='exit game'),
        ]
    ]
)

add_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='add 1000', callback_data='self add 1000')]
    ]
)

end_game_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='player with 0', callback_data='end_with_0'),
    ],
    [
        InlineKeyboardButton(text='player with chips', callback_data='add_funds'),
    ],
    [
        InlineKeyboardButton(text='end game', callback_data='end_game'),
    ],
]
)

add_admin_keyboard = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='add player', callback_data='add_player'),
            InlineKeyboardButton(text='add admin', callback_data='add_admin'),
            InlineKeyboardButton(text='delete admin', callback_data='delete_admin'),
        ],
    ],
)


async def get_paid_button(debt_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'DEBT {debt_id} PAID', callback_data=f'debt_{debt_id}')]])


async def get_paid_button_confirmation(debt_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'YEAH', callback_data=f'{debt_id}_yeah_debt')],
        [InlineKeyboardButton(text=f'NOPE', callback_data=f'{debt_id}_nope_debt')],
    ],
    )
