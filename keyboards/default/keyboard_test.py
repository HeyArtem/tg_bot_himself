from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

'''
это всплывающая клава, вызывается из test.py
оп команде из test.py "Любой текст"
и выводит кнопку "/menu"
'''


kb_test = ReplyKeyboardMarkup(
    keyboard=[
        
        [
            KeyboardButton(text="/menu")
        ]
    ],
    resize_keyboard=True
)
