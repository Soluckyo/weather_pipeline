from weather_client import fetch_weather
from cities import CITIES
from repository import upsert_weather, get_last_leaded_date, update_last_loaded_date
from datetime import date, timedelta


def main():
 
    last_date = get_last_leaded_date()
    today = date.today()

    if last_date:
        start_date = last_date + timedelta(days=1)
    else:
        start_date = today

    for city in CITIES:
        print(f"Fetching weather for {city.name}")
        records = fetch_weather(city, start_date=start_date, end_date=today)

        upsert_weather(records)
        print(f"City {city.name}: {len(records)} records fetched from {start_date} to {today}")
    update_last_loaded_date(today)

if __name__ == "__main__":
    main()