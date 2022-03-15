from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# здесь описываю инлайн клавиатуру
#  row_width - кол-во кнопок в одной строке (по умолчанию 3)
ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Сообщение", callback_data="Сообщение"),
                                        InlineKeyboardButton(text="Ссылка", url="https://www.youtube.com/watch?v=2Il_Ab-s0W8&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=5")
                                    ],
                                    [
                                        InlineKeyboardButton(text="alert", callback_data="alert")
                                    ],
                                    [
                                        InlineKeyboardButton(text="Заменить кнопки меню", callback_data="Кнопки2")
                                    ]
                                ])
