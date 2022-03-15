from aiogram import types
from loader import dp

'''
скрипт сообщает об ошибке
при вводе несуществующей команды
'''

@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f" Команада {message.text}! \nНЕ НАЙДЕНА!!! \n(error.py)")
