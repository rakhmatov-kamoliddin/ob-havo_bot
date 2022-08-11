
from aiogram.dispatcher import FSMContext
from keyboards.default import main_menu
from aiogram import types
from aiogram.dispatcher.filters import Text
from filters.private_filter import IsPrivate
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    # print(users[0][0])
    
    allusers=''
    for i,user in enumerate(users):
        allusers+=f'{i+1}.{user[1]}\t{user[2]}\n'
    await message.answer(allusers)

# @dp.message_handler(text="/reklama", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message, state: FSMContext):
#     await message.answer('Reklamangizni kiriting !')
#     await Reklama.reklama.set()
# @dp.message_handler(state=Reklama.reklama)
# async def online_courses(message: types.Message, state: FSMContext):
#     users = db.select_all_users()
#     for user in users:
#         user_id = user[0]
#         await bot.send_message(chat_id=user_id, text="@uz_python kanaliga obuna bo'ling!")
#         await asyncio.sleep(0.05)
        

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
    
    
    
@dp.message_handler(IsPrivate(), text="/advert", user_id=ADMINS)
async def send_ad_command(message: types.Message, state: FSMContext):
    await message.answer("Отправьте рекламу...")
    await state.set_state("advertisement")


@dp.message_handler(state = "advertisement", content_types=types.ContentType.ANY)
async def sending_advert(message: types.Message, state: FSMContext):
    state.finish()
    users = db.select_all_users()
    count = db.count_users()[0]
    
    for user in users:
        user_id = user[0]
    await bot.copy_message(user_id, message.chat.id, message.message_id)
    await message.answer(f"Реклама была отправлена {count} пользователям.")
    await state.finish()
    
    
@dp.message_handler(Text('About'))
async def bot_start(message: types.Message):
    await message.answer_photo('https://img.myloview.com/stickers/glowing-neon-line-sun-and-cloud-weather-icon-isolated-on-black-background-vector-700-240571863.jpg',caption="🌎 Dunyoning barcha shaharlarning ob-havosini topib berish uchun mo'ljalangan telegram bot!\n",reply_markup=main_menu.Menu)


@dp.message_handler(text=('/about'))
async def bot_start(message: types.Message):
    await message.answer_photo('https://img.myloview.com/stickers/glowing-neon-line-sun-and-cloud-weather-icon-isolated-on-black-background-vector-700-240571863.jpg',caption="🌎 Dunyoning barcha shaharlarning ob-havosini topib berish uchun mo'ljalangan telegram bot!\n",reply_markup=main_menu.Menu)
