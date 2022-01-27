import os
from wa_group_sender import send_message
from sqlite_connection import create_db,connect_db, run_query, preprocessing_records_db, save_records_db

db_name = "crypto_db.db"
table_name = "btc_hist"

print(f"Verificando base de datos: {db_name}")

if not os.path.exists(db_name):
    print(f"No existe en el folder de trabajo, creando {db_name}...")
    create_db(db_name)
    print(f"Creando tabla {table_name}")

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        date DATETIME,
        currency VARCHAR(50),
        price FLOAT
    );

    """
    run_query(connection=connect_db(db_name), 
        sql_query=create_table_query)
else:
    print(f"{db_name} ya existe!")
    print(f"Creando tabla si no existe {table_name}")

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        date DATETIME,
        currency VARCHAR(50),
        price FLOAT
    );

    """
    run_query(connection=connect_db(db_name), 
        sql_query=create_table_query)


if not ((os.path.exists("chromedriver.exe")) or (os.path.exists("/home/pi/Downloads/chromedriver"))):

    print(f"Does Chrome Driver Exists? {not os.path.exists('chromedriver.exe')}")
    print(f"Does Chromium Driver Exists? {not os.path.exists('/home/pi/Downloads/chromedriver')}")

    print("Please download the Chromedriver version according to your browser...")
    print("If you are using google chrome: https://chromedriver.chromium.org/downloads")
else:
    print("Getting BTC Price...")

    send_message(receiver="test_crypto")