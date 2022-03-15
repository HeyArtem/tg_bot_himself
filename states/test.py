from sre_parse import State
from aiogram.dispatcher.filters.state import StatesGroup, State


class register(StatesGroup):
    
    # в State() я храню данные в которых находится пользоватеоль
    test1 = State()
    test2 = State()
