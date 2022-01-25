from logging import warning
from multiprocessing.connection import wait
from tokenize import group

from matplotlib.pyplot import get


def send_message(receiver ="test"):
    '''
    Sends a message with the most actual price of a crypto
    Arguments:
        -receiver: name of the person or the group. It can be approximate but a precise name works better
    '''
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time
    from get_crypto_price import get_price
    from datetime import datetime
    
    try:
        driver = webdriver.Chrome("chromedriver.exe")
    except:
        driver = webdriver.Chrome("/usr/bin/chromedriver")
    driver.get("https://web.whatsapp.com")
    time.sleep(10)
    wait = WebDriverWait(driver, 600)

    target = f'{receiver}'

    x_arg = f'//span[@title="{target}"]'
    group_title = wait.until(EC.presence_of_all_elements_located((By.XPATH, x_arg)))
    print("groups that matches:" ,len(group_title))
    #[print(i.text) for i in group_title[:5]]
    group_title[0].click()

    inp_xpath = "//div[@class ='_13NKt copyable-text selectable-text'][@data-tab='10']"
    input_box = wait.until(EC.presence_of_all_elements_located((By.XPATH, inp_xpath)))
    price_story = []
    while True:
        price = get_price()
        price_int = float(price.replace(",", ""))
        price_int = round(price_int, 2)
        price_story.append(price)
        today = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        print(price)

        #if price_int >=36300:
        #    message_to_send = f"Precio BTC el {today} pasó los $36,300 USD. Precio Actual: {price}"
        #    input_box[0].send_keys(message_to_send + Keys.ENTER)
        
        print("Sleeping 5 minutes...")
        #time.sleep(300)
        
        today = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        message_to_send = f"Precio BTC el {today} ---> ${price}"
        input_box[0].send_keys(message_to_send + Keys.ENTER)
        time.sleep(300)