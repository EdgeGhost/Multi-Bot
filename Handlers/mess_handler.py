import numexpr as ne
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv,find_dotenv
from aiogram import Router,F,types
from aiogram.filters import CommandStart

from FSM.States import FunctionStates
from Keyboards.inline_kbd import start_kbd
from Keyboards.reply_kbd import back_kbd
from Utils.weather_info import weather_city,weather_lct_btn

load_dotenv(find_dotenv())
user_handler_router = Router()

async def start_mess(mess: types.Message):
    await mess.answer(f'Привет👋!, я мультифункциональный бот🤖\n'
                      f'умею повторять ваши сообщение🔤,есть встроенный калькулятор🧮,'
                      f'могу сказать о курсе валют💸 и узнать текущий прогноз погоды в вашем городе🌤,\n'
                      f'Выберите одну из них👇',
                      reply_markup=start_kbd())
@user_handler_router.message(CommandStart())
async def start(mess: types.Message):
    await start_mess(mess)

@user_handler_router.message(F.text.lower() == "назад")
async def cancel(mess: types.Message, state: FSMContext):
    await state.clear()
    await start_mess(mess)

@user_handler_router.message(FunctionStates.echo_func)
async def echo_mess(mess:types.Message):
    await mess.answer(f'Эхо: {mess.text}')

@user_handler_router.message(FunctionStates.calc_func)
async def calc_mess(mess: types.Message):
    result = ne.evaluate(mess.text).item()
    await mess.answer(f'Ответ {result}')


@user_handler_router.message(FunctionStates.phone)
async def phone_type_weather(mess: types.Message):
    result = await weather_lct_btn(mess)
    await mess.answer(f'В вашем городе температура {result}°С',
                      reply_markup=back_kbd())

@user_handler_router.message(FunctionStates.pc)
async def pc_type_weather(mess: types.Message):
    result = await weather_city(mess)
    await mess.answer(f'В вашем городе температура {result}°С',)


