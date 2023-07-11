import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text  # Фильтр для /start, /...
from aiogram.types import Message  # Тип сообщения

from config import config  # Config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет')


@dp.message(Text(text='Ответь'))
async def reply(message: Message):
    await message.reply('Ответил')


@dp.message()
async def echo_all(message: Message):
    await message.send_copy(message.chat.id)


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
