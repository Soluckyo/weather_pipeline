CREATE TABLE IF NOT EXISTS raw_weather (
    city TEXT NOT NULL,
    observation_time TIMESTAMP NOT NULL,
    temperature FLOAT,
    wind_speed FLOAT,
    precipitation FLOAT,
    ingestion_time TIMESTAMP NOT NULL DEFAULT now(),
    PRIMARY KEY(city, observation_time)
);