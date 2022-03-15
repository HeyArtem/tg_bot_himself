from loader import dp
from aiogram import types
from keyboards.inline import ikb_menu, ikb_menu2
from aiogram.types import CallbackQuery
# from handlers.users.test import kb_test

from keyboards.default import kb_test


# вызов инлайн клавиатуры (прикрепленная к сообщению)
@dp.message_handler(text="Инлайн меню")
async def show_inline_menu(message: types.Message):
    await message.answer("Инлайн кнопки ниже", reply_markup=ikb_menu)
    

# text from inline_kb_menu.py
# разные await!!! потому что text="Сообщение" -> еще и вызывает клавиатуру 
@dp.callback_query_handler(text="Сообщение")
async def send_message(call: CallbackQuery):
    await call.message.answer('Кнопки заменены (from inline_menu.py)', reply_markup=kb_test)


# выведет сообщение 'Кнопки заменены (from inline_menu.py)'
# show_alert=True -> вывод сообщения "Кнопки заменены" с требованием нажать ОК
@dp.callback_query_handler(text="alert")
async def send_message(call: CallbackQuery):
    await call.answer('Кнопки заменены (from inline_menu.py)', show_alert=True)
    
    
# кнопки2. будет отправлять сообщение "Инлайн кнопки заменены"
@dp.callback_query_handler(text="Кнопки2")
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)

