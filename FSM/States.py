from aiogram.fsm.state import State,StatesGroup

class FunctionStates(StatesGroup):
    echo_func = State()
    calc_func = State()
    weather_func = State()
    phone = State()
    pc = State()
