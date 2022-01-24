import requests
from bs4 import BeautifulSoup as BS

def get_price(url = "https://www.google.com/", sign = "BTC"):
    url = f"{url}search?q={sign}+price"
    data = requests.get(url)

    return data.text

print(get_price())
