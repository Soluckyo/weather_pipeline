from collections import namedtuple
from datetime import datetime

WeatherRecord = namedtuple("WeatherRecord", ["city", "temperature", "wind_speed", "precipitation", "observation_time"])

def parse_weather_data(city, data):
    records = []
    hourly = data.get("hourly", {})
    temperatures = hourly.get("temperature_2m", [])
    wind_speeds = hourly.get("windspeed_10m", [])
    precipitations = hourly.get("precipitation", [])
    times = hourly.get("time", [])

    for i in range(len(times)):
        dt = datetime.fromisoformat(times[i])
        # измерения только 0, 6, 12, 18 часов
        if dt.hour in [0, 6, 12, 18] and dt.minute == 0:
            temp = temperatures[i]
            if temp is None:
                continue  #пропускаем записи без температуры
            record = WeatherRecord(
                city=city.name,
                temperature=temp,
                wind_speed=wind_speeds[i],
                precipitation=precipitations[i],
                observation_time=dt
            )
            records.append(record)

    return records