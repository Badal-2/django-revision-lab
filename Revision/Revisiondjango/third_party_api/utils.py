import requests
from django.conf import settings

def get_crypto_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {"X-CMC_PRO_API_KEY": settings.COINMARKETCAP_API}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data']  # <-- You forgot this line in the second copy
