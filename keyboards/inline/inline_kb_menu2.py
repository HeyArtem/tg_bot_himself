from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Сообщение (inline_kb_menu2)", callback_data="Сообщение"),
                                        InlineKeyboardButton(text="Ссылка (inline_kb_menu2)", url="https://www.youtube.com/watch?v=2Il_Ab-s0W8&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=5")
                                    ]
                                ])
