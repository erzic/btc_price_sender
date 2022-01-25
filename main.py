import os
if not os.path.exists("chromedriver.exe"):
    print("Please download the Chromedriver version according to your browser...")
    print("If you are using google chrome: https://chromedriver.chromium.org/downloads")
else:
    print("Getting BTC Price")