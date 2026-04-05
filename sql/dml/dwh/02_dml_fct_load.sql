--заполение таблицы фактов load_fct_weather
WITH ranked as(select dc.city_id, 
			sw.obs_date, 
			sw.obs_hour, 
			sw.temperature, 
			sw.wind_speed, 
			sw.precipitation, 
	        row_number() over(partition by sw.obs_date, sw.obs_hour, sw.city order by sw.ingestion_time) as rn
	   from stg_weather sw 
	   join dim_city dc on dc.city_name = sw.city
	  where ingestion_time > coalesce((select em.last_loaded_date 
	  									 from etl_metadata em 
	  								    where em.pipeline_name = 'fct_weather')
	  								  ,'1970-01-01')
	  								  )
insert into fct_weather(city_id, obs_date, obs_hour, temperature, wind_speed, precipitation, ingestion_time)
select city_id, obs_date, obs_hour, temperature, wind_speed, precipitation, now()
  from ranked
 where rn = 1
    on conflict(city_id, obs_date, obs_hour) do update
   set temperature = excluded.temperature,
       wind_speed = excluded.wind_speed,
       precipitation = excluded.precipitation;

       

--обновление metadata
insert into etl_metadata(pipeline_name, last_loaded_date)
values('fct_weather', now())
on conflict(pipeline_name) do update
set last_loaded_date = excluded.last_loaded_date;
 