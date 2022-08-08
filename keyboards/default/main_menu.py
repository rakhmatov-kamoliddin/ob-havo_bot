from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

Menu = ReplyKeyboardMarkup(
    keyboard = [
        [
        KeyboardButton(text='🌤 Weather 🌤'),
    ],
        [
        KeyboardButton(text='About'),
        KeyboardButton(text='More...'),
    ],
        ],
    resize_keyboard=True
)
