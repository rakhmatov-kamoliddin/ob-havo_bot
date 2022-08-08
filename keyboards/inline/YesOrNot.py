from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

YorN = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yes", callback_data="Yes")
            ],
        [
            InlineKeyboardButton(text="No", callback_data="No")
            ],
    ],
)

Post = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Post🖼", callback_data="post")
            ],
    ],
)