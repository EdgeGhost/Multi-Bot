import os
import requests

from aiogram.types import Message
from dotenv import load_dotenv, find_dotenv

load_dotenv((find_dotenv()))

async def weather_lct_btn(mess: Message):
    lat = mess.location.latitude
    long = mess.location.longitude
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{long}?unitGroup=metric&key={os.getenv('WEATHER_API')}'
    response = requests.get(url)
    data = response.json()
    tempinfo = data["currentConditions"]["temp"]
    return tempinfo

async def weather_city(mess: Message):
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{mess.text}?unitGroup=metric&lan=ru&key={os.getenv('WEATHER_API')}'
    response = requests.get(url)
    data = response.json()
    tempinfo = data["currentConditions"]["temp"]
    return tempinfo