import os
#import telebot
import requests
from secret import API_KEY, CHAT_ID

message_to_send = "Mensaje de prueba22"

sending_url = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={message_to_send}'

for i in range(10):
    requests.get(sending_url)
    print(2)