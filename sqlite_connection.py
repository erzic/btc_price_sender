import sqlite3
from sqlite3 import Error
from datetime import datetime

def connect_db(db_path):
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        print(f"Database {db_path} connected successfully!!")
    except Error as e:
        print(f"An Error has occurred: {e}")
    
    return connection

def run_query(connection, sql_query):
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
        connection.commit()
        print("Query ran!!")
    except Error as e:
        print(f"Query failed: {e}")

query = """
CREATE TABLE IF NOT EXISTS btc_hist (
    date DATETIME,
    currency VARCHAR(50) NOT NULL,
    price FLOAT
);
"""

now_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
currency_str = "BTC"
price = 30000.01
print(now_date)
print(type(now_date))

query_add_records = f"""
INSERT INTO
btc_hist (date, currency, price)
VALUES
    ("{now_date}", "{currency_str}", {price});
"""

run_query(
    connection=connect_db("crypto_db.db"), 
    sql_query=query_add_records)
