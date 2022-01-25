from traceback import print_exception
import requests
from bs4 import BeautifulSoup as BS

def get_price(url = "https://www.google.com/", sign = "BTC", currency = "usd"):
    url = f"{url}search?q={sign}+price+{currency}"
    print(url)
    data = requests.get(url)

    soup = BS(data.text, "html.parser")

    btc_info = soup.find("div", class_  = "BNeawe iBp4i AP7Wnd")

    price = btc_info.text
    price = price.split(" ")[0]

    #return soup.prettify()
    return price

print(get_price())
