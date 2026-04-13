from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from load_raw import load_raw
from sql_runner import run_sql_folder
from db import get_connection
from init_tables import init_tables
from config import STG_DIR, DWH_DIR, MART_DIR
from logger import get_logger

logger = get_logger(__name__)

def run_stg():
    logger.warning("--- run stg ---")
    conn = get_connection()
    try:
        run_sql_folder(conn, STG_DIR)
    finally:
        conn.close()
    logger.warning("--- end stg ---")


def run_dwh():
    logger.warning("--- run dwh ---")
    conn = get_connection()
    try:
        run_sql_folder(conn, DWH_DIR)
    finally:
        conn.close()
    logger.warning("--- end dwh ---")

def run_mart():
    logger.warning("--- run mart ---")
    conn = get_connection()
    try:
        run_sql_folder(conn, MART_DIR)
    finally:
        conn.close()
    logger.warning("--- end mart ---")

default_args = {
    "owner": "soluckyo",
    "start_date": datetime(2026, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="weather_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    raw = PythonOperator(
        task_id="load_raw",
        python_callable=load_raw
    )

    stg = PythonOperator(
        task_id="load_stg",
        python_callable=run_stg
    )

    dwh = PythonOperator(
        task_id="load_dwh",
        python_callable=run_dwh
    )

    mart = PythonOperator(
        task_id="load_mart",
        python_callable=run_mart
    )

    raw >> stg >> dwh >> mart