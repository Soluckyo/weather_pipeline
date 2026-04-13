from dataclasses import dataclass
from datetime import datetime

@dataclass
class City:
    name: str
    latitude: float
    longitude: float

@dataclass
class WeatherRecord:
    city: str
    temperature: float
    wind_speed: float
    precipitation: float
    observation_time: datetime