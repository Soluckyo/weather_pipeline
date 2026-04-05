--create table mart_city_stats
create table mart_city_stats(
	city_name text not null,
	avg_temp numeric,
	min_temp numeric,
	max_temp numeric,
	avg_wind_speed numeric,
	load_date timestamp);