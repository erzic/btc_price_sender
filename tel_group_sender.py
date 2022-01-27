def telegram_send_message(crypto_to_send = "BTC"):
    import requests
    import time
    from secret import API_KEY, CHAT_ID
    from get_crypto_price import get_price
    from datetime import datetime
    from sqlite_connection import connect_db, run_query, preprocessing_records_db, save_records_db


    sending_url = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={message_to_send}'

    price_story = []
    dates = []
    sign = []

    record_count = 0
    send_count = 0

    while True:
        price = get_price(crypto_sign=crypto_to_send)
        price_int = float(price.replace(",", ""))
        price_int = round(price_int, 2)

        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        price_story.append(price_int)
        dates.append(today)
        sign.append(crypto_to_send)

        print(price)
        record_count += 1
        send_count += 1

        if record_count == 5:
            print("Adding values to database...")
            
            records = preprocessing_records_db(dates_list=dates, sign_list=sign, price_list=price_story)
            save_records_db(table = "btc_hist", db = "crypto_db.db",records=records)
            
            print(f"Records added: {len(price_story)}")

            price_story, dates, sign = [], [], []
            record_count = 0
        
        if send_count == 5:
            message_to_send = f"Precio BTC el {today} ---> ${price}"
            sending_url = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={CHAT_ID}&text={message_to_send}'
            requests.get(sending_url)
            send_count = 0