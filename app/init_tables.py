from db import get_connection
from sql_runner import run_sql_folder
from config import DDL_DIR

def init_tables():
    conn = get_connection()
    try:
        run_sql_folder(conn, DDL_DIR)
    finally:
        conn.close()
