from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor


'''
Урок 1

Изучаю tg bot, хочу узнать машину состояний
по видео
https://www.youtube.com/watch?v=FRUKYZtOaSM&t=37s
'''

# создаем переменную бота
bot = Bot(token='!!!ЗДЕСЬ ВПИСАТЬ СВОЙ ТОКЕН!!!')

# диспетчер
dp = Dispatcher(bot=bot)

# если в скобках ни чего нет, то бот будет отвечать на любую команду
@dp.message_handler()

# если в скобках написано "message: types.Message", то в скрипте мы используем "message" вместо "types.Message"
async def get_message(message: types.Message):
    
    # получим id пользователя
    #  I вар.
    # chat_id = types.Message.chat.id
    
    # # II вар.
    # chat_id_2 = message.chat.id
    # text_2 = "Hello chat_id_2!"
    # await bot.send_message(chat_id=chat_id_2, text=text_2)
    
    # text_3 = "What the Text 3?"
    # await message.answer(text=text_3)
    
    # # здесь бот будет отвечать тем же текстом, которым его вызвали
    # text = message.text
    # await message.answer(text=text)
    
    # бот будет отвечать тебе привет + твое имя
    text = f"Привет {message.from_user.full_name}"
    await message.answer(text=text)
    
    # парралельно выведу в консоль инфу
    # текст сообщения, которым вызвали
    print(message.text)
    
    # имя пользователя
    print(message.from_user.full_name)
    
    # инфу о пользователе
    print(message.from_user)
    
    # id пользователя который пишет нашему боту
    print(message.from_user.id)
    


executor.start_polling(dp)

