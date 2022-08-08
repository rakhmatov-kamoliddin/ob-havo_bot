from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp,bot


# Echo bot
@dp.message_handler(Command('toadmin'))
async def bot_echo(message: types.Message, state: FSMContext):
    
    await message.answer('Savol va e\'tirozlaringizni kiriting')
    
    await state.set_state("toadmin")

@dp.message_handler(state="toadmin")
async def enter_email(message: types.Message, state: FSMContext):
    from_chat_id=message.from_id
    message_id=message.message_id
    msg = message.text
    await state.finish()
    await bot.forward_message(chat_id=ADMINS[0], from_chat_id=from_chat_id,message_id=message_id)

# @dp.message_handler(user_id=ADMINS)
# async def enter_email(message: types.Message, state: FSMContext):
#     chat_id=message.reply_to_message.forward_from['id']
#     text=message.text
#     print(chat_id)
#     await bot.send_message(chat_id=chat_id,text=text)



# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)