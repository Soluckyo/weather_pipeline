--create table mart_city_stats
\connect weather;

CREATE TABLE IF NOT EXISTS mart_city_stats(
	city_name text not null,
	avg_temp numeric,
	min_temp numeric,
	max_temp numeric,
	avg_wind_speed numeric,
	load_date timestamp);