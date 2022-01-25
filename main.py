import os

from matplotlib.pyplot import get
from get_crypto_price import get_price

from wa_group_sender import send_message

if not os.path.exists("chromedriver.exe"):
    print("Please download the Chromedriver version according to your browser...")
    print("If you are using google chrome: https://chromedriver.chromium.org/downloads")
else:
    print("Getting BTC Price...")

    send_message(receiver="test_crypto")