import requests
import time
from datetime import datetime, timedelta
from models import WeatherRecord
from config import BASE_URL 
from logger import get_logger
from parse import parse_weather_data

logger = get_logger(__name__)

MAX_RETRIES = 3
RETRY_DELAY = 5

#получаем данные за день
def fetch_weather_one_day(city, single_date):
    params = {
        "latitude": city.latitude,
        "longitude": city.longitude,
        "hourly": "temperature_2m,precipitation,windspeed_10m",
        "start_date": single_date.isoformat(),
        "end_date": single_date.isoformat()
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(BASE_URL, params = params, timeout=10)
            response.raise_for_status
            data = response.json()

            if "hourly" not in data or not data["hourly"]["temperature_2m"]:
                logger.warning("No data for %s on %s, skip", city.name, single_date)
                return []
            
            #парсим данные
            records = parse_weather_data(city, data)
            return records
        except requests.exceptions.RequestException as e:
            logger.warning("Attempt %s failed for %s on %s: %s", attempt, city.name, single_date, e)
            time.sleep(RETRY_DELAY)
    logger.error("Failed to fetch data for %s on %s after %s retries", city.name, single_date, MAX_RETRIES)
    return []

#разбиваем на дни
def fetch_weather(city, start_date, end_date):
    all_records = []
    current_date = start_date
    while current_date <= end_date:
        daily_records = fetch_weather_one_day(city, current_date)
        all_records.extend(daily_records)
        current_date += timedelta(days=1)
    return all_records