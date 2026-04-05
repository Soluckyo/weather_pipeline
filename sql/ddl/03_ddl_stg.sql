create table stg_weather(
	city text,
	obs_date date,
	obs_hour int,
	temperature int,
	wind_speed float8,
	precipitation float8,
	ingestion_time timestamp);

ALTER TABLE stg_weather
ADD CONSTRAINT stg_weather_pk PRIMARY KEY (city, obs_date, obs_hour);