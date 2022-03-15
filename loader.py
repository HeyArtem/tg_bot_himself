from aiogram import Bot, types, Dispatcher
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)



# создаю хранилище оперативной памяти
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
# dp = Dispatcher(bot)

