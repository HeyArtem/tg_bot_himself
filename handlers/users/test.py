from aiogram import types
from loader import dp
from keyboards.default import kb_test


# это всплывающая клава
@dp.message_handler(text="Любой текст")
async def command_test(message: types.Message):
    # второй параметр ссылается на клавиатуру 'kb_test'
    await message.answer(f" Привет {message.from_user.full_name}! \n"
                         f"тут должен быть какой то текст \n(test.py)", reply_markup=kb_test)
