from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

Courses = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text='🧑‍💻 Связатся с админом',callback_data='admin'),
    ],
        [
        InlineKeyboardButton(text='☎ Контакты.....',url='https://t.me/rakhmat0v_2007'),
        InlineKeyboardButton(text='📩 Поделиться....',switch_inline_query="Dunyoning barcha shaharlarning ob-havosini topib berish uchun mo'ljalangan telegram bot"),
    ],
    #     [
    #     InlineKeyboardButton(text='🔍 Qidirish....',switch_inline_query_current_chat=""),
    # ],
        ],
    # resize_keyboard=True
)