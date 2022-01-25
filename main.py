import os

from matplotlib.pyplot import get
from get_crypto_price import get_price
from datetime import datetime
from wa_group_sender import send_message

if not os.path.exists("chromedriver.exe"):
    print("Please download the Chromedriver version according to your browser...")
    print("If you are using google chrome: https://chromedriver.chromium.org/downloads")
else:
    print("Getting BTC Price...")
    
    price = get_price()
    today = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    message_to_send = f"Precio BTC el {today} ---> ${price}"
    print(message_to_send)

    send_message(message=message_to_send, receiver="test_crypto")