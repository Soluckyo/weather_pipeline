--create table mart_precipitation_daily
create table mart_precipitation_daily(
	city_name text not null,
	obs_date date,
	total_precipitation numeric,
	load_date timestamp);