from aiogram import types
from loader import dp

'''
скрипт ловит команды кнопок
если в хэндлере напишешь команду со "/", НЕ СРАБОТАЕТ!
'''

@dp.message_handler(text="10")
async def buttons_test(message: types.Message):
    await message.answer(f" Привет {message.from_user.full_name}! \n"
                         f"Ты выбрал: число {message.text}! \n(buttons.py)")


@dp.message_handler(text="11")
async def buttons_test(message: types.Message):
    await message.answer(f" Привет {message.from_user.full_name}! \n"
                         f"Ты выбрал: число {message.text}! \n(buttons.py)")


@dp.message_handler(text="100")
async def buttons_test(message: types.Message):
    await message.answer(f" Привет {message.from_user.full_name}! \n"
                         f"Ты выбрал: число {message.text}! \n(buttons.py)")
