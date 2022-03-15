from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers import dp #это надо?
from aiogram import executor



async def on_startup(dp):
    
    await on_startup_notify(dp)    
    
    await set_default_commands(dp)
    
    # выводится в терминал
    print("Бот запущен! (app.py)")
    

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)