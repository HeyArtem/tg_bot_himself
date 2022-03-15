from aiogram import types
from loader import dp


@dp.message_handler(text="/zhopa")
async def command_zhopa(message: types.Message):
    await message.answer(f" Привет zhopa \n(users/zhopa.py)")
