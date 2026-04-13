import psycopg2
from pathlib import Path
from logger import get_logger

logger = get_logger(__name__)

def run_sql_file(conn, file_path):
    logger.warning(f"START SQL: {file_path}")
    try: 
        with open(file_path, "r") as f:
            sql = f.read()
        
        with conn.cursor() as cur:
            cur.execute(sql)

        conn.commit()
        logger.warning(f"SUCCESS SQL: {file_path}")
    except Exception as e:
        logger.error(f"FAILED SQL: {file_path}")
        logger.error(str(e))
        conn.rollback()
        raise

def run_sql_folder(conn, folder_path):
    files = sorted(Path(folder_path).glob("*.sql"))

    for file in files:
        logger.warning(f"Running sql script {file.name}")
        run_sql_file(conn, file)