--создание таблицы погоды
\connect weather;

CREATE TABLE IF NOT EXISTS fct_weather(
city_id int not null,
obs_date date not null,
obs_hour int not null,
temperature int,
wind_speed float8,
precipitation float8,
ingestion_time timestamp,

primary key(city_id, obs_date, obs_hour),

constraint fk_city
	foreign key(city_id)
	references dim_city(city_id)
);

	