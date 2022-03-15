from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# фаил menu.py обращается к этим кнопкам
kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        
        # превый ряд кнопок
        [
            KeyboardButton(text="10"),
            KeyboardButton(text="11")
        ],
        
        # второй ряд кнопок
        [
            KeyboardButton(text="100")
        ],
        
        # третий ряд кнопок
        [
            KeyboardButton(text="Инлайн меню"),
            KeyboardButton(text="Любой текст"),
            KeyboardButton(text="Лайк"),
        ]
    ],
    resize_keyboard=True
)
