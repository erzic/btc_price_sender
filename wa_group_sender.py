from logging import warning
from multiprocessing.connection import wait
from tokenize import group


def send_message(message= "Holaa con dos a", person_id ="1"):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://web.whatsapp.com")
    wait = WebDriverWait(driver, 600)

    target = "test" 

    x_arg = f"//span[contains(@title,{target})"
    group_title = wait.until(EC.presence_of_all_elements_located((By.XPATH, x_arg)))
    group_title.click()

    inp_xpath = "//div[@class ='_13NKt copyable-text selectable-text'][@data-tab='10']"
    input_box = wait.until(EC.presence_of_all_elements_located((By.XPATH, inp_xpath)))

    for i in range(4):
        input_box.send_keys(message + Keys.ENTER)



send_message()