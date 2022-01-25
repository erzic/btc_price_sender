from logging import warning
from multiprocessing.connection import wait
from tokenize import group

from matplotlib.pyplot import get
from get_crypto_price import get_price

def send_message(message= "Holaa con dos a", receiver ="test"):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome("chromedriver.exe")
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

    for i in range(100):
        input_box[0].send_keys(message + Keys.ENTER)