from aiogram import Router,F,types
from aiogram.fsm.context import FSMContext

from FSM.States import FunctionStates
from Keyboards.inline_kbd import survey_kbd
from Keyboards.reply_kbd import loction_kbd
from Utils.exchange_rate import get_exchange_rate

user_callback_router = Router()

@user_callback_router.callback_query(F.data.startswith('echo_'))
async def echo(call: types.CallbackQuery,state:FSMContext):
    await call.answer()
    await call.message.answer('Вы перешли на функцию эхо бота\n'
                      'Отправляйте любые сообщение я буду их повторять\n'
                      'Чтобы выйти напишите "Назад"')
    await state.set_state(FunctionStates.echo_func)

@user_callback_router.callback_query(F.data.startswith('calc_'))
async def calc(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Вы перешли на функцию калькулятора\n'
                              'Отправьте любые математические выражение\n'
                              'Я отправлю вам ответ')
    await state.set_state(FunctionStates.calc_func)

@user_callback_router.callback_query(F.data.startswith('weather_'))
async def get_weather(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('Пережде чем приступить к работе\n'
                              'Ответь на вопрос\n'
                              'На каком устроистве вы сидите?',
                              reply_markup=survey_kbd())

@user_callback_router.callback_query(F.data.startswith('phone_'))
async def weather_phone_edition(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer(f'Вы перешли на функцию о прогнозе погоды\n'
                        f'Чтобы узнать текущею погоду\n'
                        f'Нажмите на кнопку ниже чтобы поделиться своим '
                        f'местоположением',reply_markup=loction_kbd())
    await state.set_state(FunctionStates.phone)

@user_callback_router.callback_query(F.data.startswith('PC_'))
async def weather_pc_edition(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer('Вы перешли на функцию о прогнозе погоды\n'
                              ' Чтобы узнать текущею погоду\n'
                              'Введите свой город\n')
    await state.set_state(FunctionStates.pc)

@user_callback_router.callback_query(F.data.startswith('excrate_'))
async def exc_rate(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('Вы перешли функцию о курс валют\n'
                              'На данный момент доступны только три')
    print("[DEBUG] exchange_rate хендлер вызван")
    result = get_exchange_rate()
    if result:
        await call.message.answer(f'Доллар(USD): {result[0]} тенге(KZT)\n'
                          f'Евро(EURO): {result[1]} тенге(KZT)\n'
                          f'Рубль(RUB): {result[2]} тенге(KZT)')
    else:
        await call.message.answer('Ошибка')