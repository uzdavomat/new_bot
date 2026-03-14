import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import  Command
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN=os.getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f"hello {message.from_user.first_name}")


@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('kljhgfdzgxchvjkjl;')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

