import os

from matplotlib.pyplot import get
from get_crypto_price import get_price

from wa_group_sender import send_message

if not ((os.path.exists("chromedriver.exe")) or (os.path.exists("/home/pi/Downloads/chromedriver"))):

    print(f"Does Chrome Driver Exists? {not os.path.exists('chromedriver.exe')}")
    print(f"Does Chromium Driver Exists? {not os.path.exists('/home/pi/Downloads/chromedriver')}")

    print("Please download the Chromedriver version according to your browser...")
    print("If you are using google chrome: https://chromedriver.chromium.org/downloads")
else:
    print("Getting BTC Price...")

    send_message(receiver="test_crypto")