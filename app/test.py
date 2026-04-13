from datetime import date
from weather_client import fetch_weather
from cities import CITIES

city = CITIES[0]  # первый город
records = fetch_weather(city, start_date=date(2026,3,9), end_date=date(2026,3,9))
for r in records:
    print(r.observation_time, r.temperature, r.wind_speed, r.precipitation)