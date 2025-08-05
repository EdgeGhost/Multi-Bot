import requests
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
# def get_exchange_rate():
#     rub = 'RUB'
#     eur = 'EUR'
#     usd = 'USD'
#     kzt = 'KZT'
#     url_rub = f"https://api.exchangerate.host/convert?from={rub}&to={kzt}&amount=1&access_key={os.getenv('VALUE_CURSE_API')}"
#     response_rub = requests.get(url_rub)
#     data_rub = response_rub.json()
#     rub_to_tenge = data_rub['result']
#     print(rub_to_tenge)
#     url_usd = f"https://api.exchangerate.host/convert?from={usd}&to={kzt}&amount=1&access_key={os.getenv('VALUE_CURSE_API')}"
#     response_usd = requests.get(url_usd)
#     data_usd = response_usd.json()
#     print(data_usd)
#     usd_to_tenge = data_usd['result']
#     print(usd_to_tenge)
#     url_eur = f"https://api.exchangerate.host/convert?from={eur}&to={kzt}&amount=1&access_key={os.getenv('VALUE_CURSE_API')}"
#     response_eur = requests.get(url_eur)
#     data_eur = response_eur.json()
#     eur_to_tenge = data_eur['result']
#     print(eur_to_tenge)
#     return [round(usd_to_tenge, 2), round(eur_to_tenge, 2), round(rub_to_tenge, 2)]
#
# get_exchange_rate()

url = f"https://api.exchangerate.host/convert?from=USD&to=KZT&amount=1"
response_eur = requests.get(url)
data_eur = response_eur.json()
print(data_eur)
# eur_to_tenge = data_eur['result']
# print(eur_to_tenge)
# &access_key={os.getenv('VALUE_CURSE_API')}