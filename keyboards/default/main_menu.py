from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

Menu = ReplyKeyboardMarkup(
    keyboard = [
        [
        KeyboardButton(text='🌤 Погода 🌤'),
    ],
        [
        KeyboardButton(text='Информация о боте'),
        KeyboardButton(text='Дополнительно...'),
    ],
        ],
    resize_keyboard=True
)
