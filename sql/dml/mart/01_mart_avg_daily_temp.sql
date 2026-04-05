--load mart avg_temp_daily
truncate table mart_avg_temp_daily;

insert into mart_avg_temp_daily
select avg(fw.temperature) as avg_temp
	  ,dc.city_name
	  ,fw.obs_date
	  ,now()
  from fct_weather fw
  join dim_city dc on dc.city_id = fw.city_id 
 group by dc.city_name, fw.obs_date 
 order by fw.obs_date DESC;
 
 --обновление metadata
insert into etl_metadata(pipeline_name, last_loaded_date)
values('mart_avg_temp_daily', now())
on conflict(pipeline_name) do update
set last_loaded_date = excluded.last_loaded_date;
