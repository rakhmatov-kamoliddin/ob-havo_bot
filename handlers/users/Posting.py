# from gc import callbacks
from aiogram import types
# from data.config import CHANNELS
from loader import dp
# from keyboards.inline import YesOrNot
# from keyboards.default import main_menu
from aiogram.dispatcher.filters.builtin import Text
# from states.posting_on_channel import Post,Weater
from aiogram.dispatcher import FSMContext
import requests
import datetime
from aiogram import *

open_weather_token = "9a3bd9f125cbd2e9b79eeee6c71cee41"

@dp.message_handler(Text('🌤 Погода 🌤'))
async def bot_start(message: types.Message, state: FSMContext):
    await message.reply("Привет! Напиши мне название города и я отправлю тебе прогноз погоды!")
    @dp.message_handler()
    async def get_weather(message: types.Message, state: FSMContext):
            
            code_to_smile = {
                "Clear": "\U00002600  Ясно \U00002600",
                "Clouds": "\U00002601  Облачно \U00002601",
                "Rain": "\U00002614  Дождь \U00002614",
                "Drizzle": "\U00002614  Дождь \U00002614",
                "Thunderstorm": "\U000026A1  Гроза \U000026A1",
                "Snow": "\U0001F328  Снег \U0001F328",
                "Mist": "\U0001F32B  Туман \U0001F32B"
            }

            try:
                r = requests.get(
                    f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
                )
                data = r.json()

                city = data["name"]
                cur_weather = data["main"]["temp"]

                weather_description = data["weather"][0]["main"]
                if weather_description in code_to_smile:
                    wd = code_to_smile[weather_description]
                else:
                    wd = "Посмотри в окно, не пойму что там за погода!"

                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind = data["wind"]["speed"]
                sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
                sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
                length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                    data["sys"]["sunrise"])
                
                await message.reply(
                    f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                    f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
                    f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                    f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                    f"***Хорошего дня!***"
                    )
                
            except:
                await message.reply("\U00002620 Проверьте название города \U00002620")
            






# @dp.callback_query_handler(text="post")
# async def bot_content(call: types.CallbackQuery,state: FSMContext):

#         await state.update_data({"content" : str(call.message.text)})
#         await call.message.answer("Do you want to post this?\n", reply_markup=YesOrNot.YorN)
        

# @dp.callback_query_handler(text="Yes")
# async def online_courses(call: types.CallbackQuery, state: FSMContext):
#     data = await state.get_data()
#     content= data.get('content')
#     await dp.bot.send_message(CHANNELS[0], content)
#     await call.message.delete()
#     await call.message.answer("Posted", reply_markup=main_menu.Menu)
    

# @dp.callback_query_handler(text="No")
# async def online_courses(call: types.CallbackQuery, state: FSMContext):

#     await call.message.delete()
#     await call.message.answer("Menu", reply_markup=main_menu.Menu)

