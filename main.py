import os
from wa_group_sender import send_message
from sqlite_connection import create_db,connect_db, run_query, preprocessing_records_db, save_records_db
from tel_group_sender import telegram_send_message

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

print("Getting BTC Price...")
telegram_send_message()