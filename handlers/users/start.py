from aiogram import types
from loader import dp
import logging


@dp.message_handler(text="/start")
async def command_start(message: types.Message):
    logging.info('abra_kadabra')
        # print("JOIN message removed")
    await message.answer(f" Привет {message.from_user.full_name}! \nТвой id: {message.from_user.id} \n(start.py)")
