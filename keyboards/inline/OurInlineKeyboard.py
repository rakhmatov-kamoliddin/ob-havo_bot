from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

Courses = InlineKeyboardMarkup(
    inline_keyboard = [
        [
        InlineKeyboardButton(text='🧑‍💻 Adminga yozish',callback_data='admin'),
    ],
        [
        InlineKeyboardButton(text='Bizning manzil.....',url='https://t.me/rakhmat0v_2007'),
        InlineKeyboardButton(text='📩 Ulashish....',switch_inline_query="Dunyoning barcha shaharlarning ob-havosini topib berish uchun mo'ljalangan telegram bot"),
    ],
    #     [
    #     InlineKeyboardButton(text='🔍 Qidirish....',switch_inline_query_current_chat=""),
    # ],
        ],
    # resize_keyboard=True
)