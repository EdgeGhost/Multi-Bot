from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def loction_kbd():
    geo_kbd = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Узнать местопложение',
                       request_location=True)]
    ],resize_keyboard=True)
    return geo_kbd

def back_kbd():
    back_btn = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Назад')]
    ],resize_keyboard=True)
    return back_btn