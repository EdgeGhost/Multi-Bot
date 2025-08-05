import traceback

import requests
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())
def get_exchange_rate():
    try:
        rub = 'RUB'
        eur = 'EUR'
        usd = 'USD'
        kzt = 'KZT'
        usd_url = f"https://v6.exchangerate-api.com/v6/{os.getenv('VALUE_CURSE_API')}/pair/{usd}/{kzt}"
        eur_url = f"https://v6.exchangerate-api.com/v6/{os.getenv('VALUE_CURSE_API')}/pair/{eur}/{kzt}"
        rub_url = f"https://v6.exchangerate-api.com/v6/{os.getenv('VALUE_CURSE_API')}/pair/{rub}/{kzt}"

        res_usd = requests.get(usd_url).json()
        usd_to_kzt = res_usd['conversion_rate']

        res_eur = requests.get(eur_url).json()
        eur_to_kzt = res_eur['conversion_rate']

        res_rub = requests.get(rub_url).json()
        rub_to_kzt = res_rub['conversion_rate']

        return [round(usd_to_kzt, 2), round(eur_to_kzt, 2), round(rub_to_kzt, 2)]

    except Exception as e:
        with open('error.txt,','a') as f:
            f.write(f'\nОшибка \n {traceback.format_exc()}')
        return None
