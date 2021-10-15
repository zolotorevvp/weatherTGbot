import requests
import datetime
import os
from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

load_dotenv(".env")

tg_bot_token = os.getenv("tg_bot_token")
open_weather_token = os.getenv("open_weather_token")

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


@dp.message_handler()
async def get_weather(message: types.message):
    code_to_smile = {
        "Clear": "\U00002600",
        "Clouds": "\U00002601",
        "Rain": "\U00002614",
        "Drizzle": "\U00002614",
        "Thunderstorm": "\U000026A1",
        "Snow": "\U0001F328",
        "Mist": "\U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&lang=ru&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        weather_description = data["weather"][0]["description"]
        weather_main = data["weather"][0]["main"]

        if weather_main in code_to_smile:
            wd = code_to_smile[weather_main]
        else:
            wd = "\nПосмотри в окно, не пойму что там за погода!"

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(
            f"☂️ {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} 🌡 \n"
            f"Погода в городе: {city}\nТемпература: {cur_weather} C° {weather_description} {wd}\n"
            f"Влажность: {humidity} %\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход: {sunrise_timestamp}\nЗакат: {sunset_timestamp}\n"
        )

    except Exception:
        await message.reply("🚧 Проверьте название города 🚧")


if __name__ == '__main__':
    executor.start_polling(dp)
