from weather_client import fetch_weather
from cities import CITIES
from repository import upsert_weather, get_last_leaded_date, update_last_loaded_date
from datetime import date, timedelta
from logger import get_logger
from validation import is_valid_record


def main():
    logger = get_logger(__name__)
    last_date = get_last_leaded_date()
    today = date.today()
    DEFAULT_START_DATE = date(2026, 1, 1)

    start_date = last_date + timedelta(days=1) if last_date else DEFAULT_START_DATE

    for city in CITIES:
        logger.warning(f"Fetching weather for {city.name}")

        records = fetch_weather(city, start_date=start_date, end_date=today)

        #Проверка на валидность данных и логгирование невалидных
        valid_records = []
        invalid_count = 0

        for r in records:
            if is_valid_record(r):
                valid_records.append(r)
            else:
                invalid_count += 1

        logger.warning("City %s: %s invalid records filtered", city.name, invalid_count)

        upsert_weather(valid_records)
        #print(f"City {city.name}: {len(records)} records fetched from {start_date} to {today}")
        logger.warning(f"City {city.name}: {len(records)} records fetched from {start_date} to {today}")
    update_last_loaded_date(today)

if __name__ == "__main__":
    main()