from aiogram import types
from loader import dp

# хэндлер срвботает на команду "/привет", ему не важно, что написано в set_bot_commands.py
@dp.message_handler(text="/привет")
async def command_hello(message: types.Message):
    await message.answer(f" Привет {message.from_user.full_name}! \n Это скрипт hello.py (from users) ")
