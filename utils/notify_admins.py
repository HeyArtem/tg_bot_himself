import logging
from aiogram import Dispatcher
from data.config import admins_id


async def on_startup_notify(dp: Dispatcher):
    logging.basicConfig(level=logging.INFO, filename='example.log')
    
    for admin in admins_id:
        try:
            # сообщение которое будет отправляться в
            text = "iA-> from def on_startup_notify:\n bot is running! "
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            print("ушел в except")
            # logging.exception(err)
