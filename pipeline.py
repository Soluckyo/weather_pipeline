from load_raw import load_raw
from sql_runner import run_sql_folder
from db import get_connection
from config import STG_DIR, DWH_DIR, MART_DIR
from logger import get_logger


def run_pipeline():
    logger = get_logger(__name__)
    conn = get_connection()

    load_raw()

    logger.warning(f"Running {STG_DIR}")
    run_sql_folder(conn, STG_DIR)

    logger.warning(f"Running {DWH_DIR}")
    run_sql_folder(conn, DWH_DIR)

    logger.warning(f"Running {MART_DIR}")
    run_sql_folder(conn, MART_DIR)
    logger.warning("Complete pipeline")


if __name__ == "__main__":
    run_pipeline()
