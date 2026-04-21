import psycopg2
from psycopg2 import pool
import time
import os

connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)

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

def get_pool_connection():
    return connection_pool.getconn()

def release_pool_connection(conn):
    connection_pool.putconn(conn)