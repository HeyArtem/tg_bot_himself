
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from states import register
from aiogram.dispatcher import FSMContext

'''
После того, как пользователь отпр. команд. "/register"
бот отвечает "Привет, ты начал реги......."
и он попадает в состояние test1
'''
@dp.message_handler(Command('register'))
async def register_(message: types.Message):
    await message.answer("Привет, ты начал регистрациюб \nВведи свое имя\n(handlers/users/register.py)")
    
    # состояние ввода имени
    await register.test1.set()
    

# ловим сообщение от первого состояния
# этот хэндлер ловит все текстовые сообщения, 
# когда пользователь находится ы состоянии register.test1
@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):
    
    # сохраняю ответ пользователя
    answer = message.text
    
    # в test1 будем записывать текст который прислал нам пользователь(конретно здесь Имя)
    await state.update_data(test1=answer)
    
    # отпр. следующь. сообщ. пользователю
    await message.answer(f"{answer} сколько тебе лет?")
    
    # устанавливаю второе состояние
    await register.test2.set()


@dp.message_handler(state=register.test2)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text
    
    await state.update_data(test2=answer)
    
    data = await state.get_data()
    name = data.get("test1")
    years = data.get("test2")
    
    # # получаю имя пользователя
    # name = await state.get_data("test1")
    # # возраст пользователя
    # years = await state.get_data("test2")
    
    
    
    await message.answer(f"Регистация успешно завершена\n"
                         f"Твoе имя {name}\n"
                         f"Тебе {years} лет\n"
                         "(handlers/users/register.py)")
    

    await state.finish()
    
