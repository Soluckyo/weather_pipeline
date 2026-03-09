import requests
from datetime import datetime, timedelta
from models import WeatherRecord
from config import BASE_URL 

def fetch_weather(city, start_date, end_date):
    current_date = start_date
    records = []
    while current_date <= end_date:
        params = {
            "latitude": city.latitude,
            "longitude": city.longitude,
            "hourly": "temperature_2m,precipitation,windspeed_10m",
            "start_date": current_date.isoformat(),
            "end_date": current_date.isoformat()
        }

        response = requests.get(BASE_URL, params = params)
        data = response.json()

        if "hourly" not in data:
            print(f"No hourly data for {city.name} on {current_date}. Response: {data}")
            current_date += timedelta(days=1)
            continue

        times = data["hourly"]["time"]
        temperatures = data["hourly"]["temperature_2m"]
        wind_speeds = data["hourly"]["windspeed_10m"]
        precipitations = data["hourly"]["precipitation"]

        for i in range(len(times)):
            dt = datetime.fromisoformat(times[i])
            if dt.hour in [0,6,12,18] and dt.minute == 0:
                record = WeatherRecord(
                    city = city.name,
                    temperature = temperatures[i],
                    wind_speed = wind_speeds[i],
                    precipitation = precipitations[i],
                    observation_time = datetime.fromisoformat(times[i])
                )
                
                records.append(record)
        current_date += timedelta(days=1)

    return records



