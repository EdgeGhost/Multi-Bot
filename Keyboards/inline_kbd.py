from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def start_kbd():
    strt_kbd = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Повторять ваши сообщение(echo)',
                        callback_data='echo_')],
        [InlineKeyboardButton(text='Калькулятор',
                        callback_data='calc_')],
        [InlineKeyboardButton(text='Узнать о курсе валют',
                        callback_data='excrate_')],
        [InlineKeyboardButton(text='Узнать текущий прогноз погоды в вашем'
                             'городе',
                        callback_data='weather_')]

    ],resize_keyboard=True)
    return strt_kbd

def survey_kbd():
    srvy_kbd = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Телефон',
                              callback_data='phone_')],
        [InlineKeyboardButton(text='ПК/Ноутбук',
                              callback_data='PC_')]
    ],resize_keyboard=True)
    return srvy_kbd