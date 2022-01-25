from get_crypto_price import get_price
from datetime import datetime
from sqlite_connection import connect_db, run_query

dates = []
sign = []
price = []

for i in range(10):
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dates.append(today)
    price.append(round(float(get_price().replace(",", "")),2))
    sign.append("BTC")

def preprocessing_records_db(dates_list, sign_list, price_list):
    joined_lists = zip(dates_list, sign_list, price_list)
    values_str = ""
    for i in joined_lists:
        values_str = ",".join([values_str, str(i)])
    values_str = values_str[1:].replace("'", "\"")

    return values_str

def save_records_db(table, db, records):
    query = f"""
    INSERT INTO
    {table} (date, currency, price)
    VALUES 
        {records};
    """

    run_query(
        connection=connect_db(db), 
        sql_query=query)


records = preprocessing_records_db(dates_list=dates, sign_list=sign, price_list=price)

save_records_db(table="btc_hist", db = "crypto_db.db", records = records)