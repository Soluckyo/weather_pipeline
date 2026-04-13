import psycopg2
import time
import os


def get_connection():
    for i in range(5):  # 5 попыток
        try:
            return psycopg2.connect(
                host=os.getenv("DB_HOST"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
        except psycopg2.OperationalError:
            print("DB not ready, retrying...")
            time.sleep(3)