from aiogram import types

'''
это вывод описания команд (контекст) прописанных в users, 
описания выводятся даже если для них нет скрипта в users
'''

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "команда, запустить бота"),
        types.BotCommand("register", "регистрация"),
        types.BotCommand("help", "команда помощь"),
        types.BotCommand("hello", "он сработает на команду '/привет' "),
        types.BotCommand("zhopa", "я проверяю, что это выводится в описании"),
        types.BotCommand("prosto", "нанисал только в set_bot_commands, т.е команду не вызвать, ее не существует"),
        types.BotCommand("menu", "вызов кнопок внизу")        
    ])
