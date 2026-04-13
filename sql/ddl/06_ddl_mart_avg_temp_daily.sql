--create mart_avg_temp_daily
\connect weather;

CREATE TABLE IF NOT EXISTS mart_avg_temp_daily(
	avg_temp int,
	city_name text not null,
	obs_date date not null,
	load_date timestamp not null);