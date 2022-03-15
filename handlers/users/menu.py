from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.default import kb_menu


# почему то комманда в хэндлере пишется без "/"
@dp.message_handler(Command("menu"))  
async def menu(message: types.Message):
    # 1-й параметр (сообщение в боте), второй(вызываю клавиатуру из keyboards/default/keyboard_menu.py)
    await message.answer("Выбери число из меню ниже \n(handlers/users/menu.py)", reply_markup=kb_menu)
    