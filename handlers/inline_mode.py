import hashlib
import requests
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle,InlineQueryResultPhoto,InputMediaPhoto,InlineQueryResultGif,InputMediaAnimation,InlineQueryResultAudio,InputMediaAudio,InlineQueryResultVideo,InputMediaVideo
from loader import dp
import datetime
from aiogram import *
open_weather_token = "9a3bd9f125cbd2e9b79eeee6c71cee41"

code_to_smile = {
        "Clear": "\U00002600  Ясно \U00002600",
        "Clouds": "\U00002601  Облачно \U00002601",
        "Rain": "\U00002614  Дождь \U00002614",
        "Drizzle": "\U00002614  Дождь \U00002614",
        "Thunderstorm": "\U000026A1  Гроза \U000026A1",
        "Snow": "\U0001F328  Снег \U0001F328",
        "Mist": "\U0001F32B  Туман \U0001F32B"
    }

@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or 'weather'
    input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id=result_id,
        title=f'Result {text!r}',
        input_message_content=input_content,
        description='Shahar nomini tekshiring',
        thumb_url = 'https://img.myloview.com/stickers/glowing-neon-line-sun-and-cloud-weather-icon-isolated-on-black-background-vector-700-240571863.jpg',
        url = 'https://t.me/uzweather_bbot'

    )
    
    
    if text =='uzbekiston' or text =='Uzbekiston':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'uzbekiston'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в республике: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Uzbekiston\n{wd}',
        thumb_url = 'https://community.akamai.steamstatic.com/economy/image/omZo-YJjnL2r9xAQz5PaYyxABqBEQKXhHMDDYZt2RMqsC6O4Lc-VwDrnEkfK5whOkX7UpKSMgDxPUgdSvhp1o626ePWaqO74UYABRPDKbniorXBSXNvFLM1HVGTWwo2OlA/360fx360f',
        
    )
        
        
        
    if text =='tashkent' or text =='Tashkent':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'tashkent'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Tashkent\n{wd}',
        thumb_url = 'https://upload.wikimedia.org/wikipedia/commons/f/f7/International_Business_Center._Tashkent_city.jpg',
        
    )
        
    if text =='namangan' or text =='Namangan':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'namangan'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Namangan\n{wd}',
        thumb_url = 'https://storage.kun.uz/source/6/uR86F6RQanCrSFpOMXjvt7T08OA4onFc.jpg',
        
    )
        
    if text =='andijon' or text =='Andijon':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'Andijon'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Andijon\n{wd}',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNA_1bf_G3ptjqyLCTKfFSL-hdLqVqBLuRwLIwGaTi8jVBxqXpztjEwSM5DcQdr9BakXY&usqp=CAU',
        
    )
        
    if text =='fargona' or text =='Fargona':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'fargona'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Fargona\n{wd}',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM7RK7k2isngPgzS6DBDC4oS6g4byBXWw_h1me3MAoBh0l9gdtEa-zC6sYTxqs0-Q0Pgo&usqp=CAU',
        
    )
        
        
    if text =='guliston' or text =='Guliston':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'guliston'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Guliston\n{wd}',
        thumb_url = 'http://photos.wikimapia.org/p/00/06/80/33/09_big.jpg',
        
    )
        
        
    if text =='jizzax' or text =='Jizzax':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'jizzax'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Jizzax\n{wd}',
        thumb_url = 'https://www.agro.uz/wp-content/uploads/2021/09/jizzax-e1633417696379.jpg',
        
    )
        
        
    if text =='samarqand' or text =='Samarqand':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'samarqand'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Samarqand\n{wd}',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6-xK-AcYYcSrIDldSErzW3z5YOjQuKnThH92taQZ8PrQ7yIkuHWDZdHtL1VGvLPw0a6A&usqp=CAU',
        
    )
        
        
    if text =='qarshi' or text =='Qarshi':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'qarshi'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Qarshi\n{wd}',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6i5c10KT-NZPAJUZ6IRi21Pe7Q4ocC42415Jy3Dc4VtAi4T1SAxK22thhPGxSiltXaBM&usqp=CAU',
        
    )
        
        
    if text =='termez' or text =='Termez':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'termez'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Termez\n{wd}',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_s5Lj7ucF9O4QXg3L4_6VyFmfFZCzkSbSoSyhdm7RVCi0Hi9QKrFRQnMcLNS_QFViRnw&usqp=CAU',
        
    )
        
        
    if text =='navoiy' or text =='Navoiy':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'navoiy'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Navoiy\n{wd}',
        thumb_url = 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/7d/0c/e1/caption.jpg?w=500&h=300&s=1',
        
    )
        
        
    if text =='bukhoro' or text =='Buxoro':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'buxoro'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Buxoro\n{wd}',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMlHUpUf_Qsjk3acUaKNGGrMngtP6ErcT4Qw&usqp=CAU',
        
    )
        
        
    if text =='xiva' or text =='Xiva':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'xiva'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Xiva\n{wd}',
        thumb_url = 'https://khivamuseum.uz/sites/default/files/about_1us.png_0.jpg',
        
    )
        
        
    if text =='nukus' or text =='Nukus':

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={'nukus'}&appid={open_weather_token}&units=metric"
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

        message_w =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° \n{wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        item = InlineQueryResultArticle(
        id=result_id,
        title = f'{cur_weather} C°',
        input_message_content=InputTextMessageContent(message_w),
        description=f'Nukus\n{wd}',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjehmJz2tlldq9d0ki7Zsjc4aXro3mPDimycDixKQ3HUGHSdVKBopujm2gg53dnDjofb0&usqp=CAU',
        
    )
        
    
    await inline_query.answer(results=[item], cache_time=1)