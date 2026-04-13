--create table mart_precipitation_daily
\connect weather;

CREATE TABLE IF NOT EXISTS mart_precipitation_daily(
	city_name text not null,
	obs_date date,
	total_precipitation numeric,
	load_date timestamp);