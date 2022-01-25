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
