--load mart_precipitation_daily
truncate table mart_precipitation_daily;

insert into mart_precipitation_daily
select dc.city_name as city_name,
	   fw.obs_date as obs_date,
	   sum(fw.precipitation) as total_precipitation,
	   now() as load_date
  from fct_weather fw 
  join dim_city dc on dc.city_id = fw.city_id 
 group by fw.obs_date, dc.city_name;

 --обновление metadata
insert into etl_metadata(pipeline_name, last_loaded_date)
values('mart_precipitation_daily', now())
on conflict(pipeline_name) do update
set last_loaded_date = excluded.last_loaded_date;