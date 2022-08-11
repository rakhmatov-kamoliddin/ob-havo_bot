# from turtle import title
# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import main_menu
# from loader import dp


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=main_menu.Menu)


import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Command

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Xush kelibsiz!", reply_markup=main_menu.Menu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    
    
@dp.message_handler(Command('count'), user_id=ADMINS)
async def bot_start(message: types.Message):
    count = db.count_users()[0]
    await message.answer(f"Botda {count}-ta foydalanuvchi mavjud!")