from db import get_connection
from psycopg2.extras import execute_batch
from datetime import datetime

def upsert_weather(records):
    if not records:
        return
    
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
            INSERT INTO raw_weather(city, observation_time, temperature, wind_speed, precipitation, ingestion_time)
            VALUES(%s,%s,%s,%s,%s,%s)
            ON CONFLICT(city, observation_time) DO UPDATE
            SET temperature = EXCLUDED.temperature,
                wind_speed = EXCLUDED.wind_speed,
                precipitation = EXCLUDED.precipitation,
                ingestion_time = EXCLUDED.ingestion_time;
    """
    values = [
        (r.city, r.observation_time, r.temperature, r.wind_speed, r.precipitation, datetime.now()) 
        for r in records
        ]
    
    execute_batch(cursor, sql, values)
    conn.commit()
    cursor.close()
    conn.close()

def get_last_leaded_date(pipeline_name = "raw_weather"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT last_loaded_date FROM etl_metadata where pipeline_name = %s",
                   (pipeline_name,)
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    return row[0] if row else None

def update_last_loaded_date(date, pipeline_name="raw_weather"):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO etl_metadata(pipeline_name, last_loaded_date)
        VALUES (%s, %s)
        ON CONFLICT (pipeline_name) DO UPDATE
        SET last_loaded_date = EXCLUDED.last_loaded_date
    """
    cursor.execute(sql, (pipeline_name, date))
    conn.commit()
    cursor.close()
    conn.close()
   