from aiogram import types
from aiogram.filters import Command
from loader import dp


@dp.message(Command(commands="start"))
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")
