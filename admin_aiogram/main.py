from aiogram.filters.command import CommandStart
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from root import TOKEN, ADMIN_ID
from buttons import keyboard
from db import Database
import asyncio
import logging

db = Database("users.db")
dp = Dispatcher()

data = []


@dp.message(CommandStart())
async def start(message: Message):
    for user in db.all_userid():
        data.append(user[0])
    if message.from_user.id in data:
        if message.from_user.id == ADMIN_ID:
            await message.answer("Hello admin!", reply_markup=keyboard)
        elif message.from_user.id != ADMIN_ID:
            await message.answer("siz avval botga start bosgansiz!")  # noqa

    else:
        db.add_user(message.from_user.id, message.from_user.full_name)


@dp.message(F.text == "Chat users")
async def chat_users(message: Message, bot: Bot):
    for user in db.all_userid():
        await bot.send_message(chat_id=user[0], text="hello")


@dp.message(F.text == "Bot users")
async def bot_users(message: Message):
    count = 0
    for user in db.all_userid():
        count += 1
    await message.answer(f"👩‍💼 Bot Users: {count} ")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())