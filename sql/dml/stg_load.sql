--загрузка STG
insert into stg_weather(city, obs_date, obs_hour, temperature, wind_speed, precipitation, ingestion_time)
select rw.city,
		  rw.observation_time::date as obs_date,
		  extract(hour from rw.observation_time) as obs_hour,
		  rw.temperature as temperature,
		  rw.wind_speed as wind_speed,
		  rw.precipitation as precipitation,
		  rw.ingestion_time as ingestion_time
   from raw_weather rw
  where ingestion_time > coalesce((select em.last_loaded_date 
  									 from etl_metadata em 
  									where em.pipeline_name = 'weather_stg_pipeline')
  								  ,'1970-01-01')
  
 
--обновление metadata
insert into etl_metadata(pipeline_name, last_loaded_date)
values('weather_stg_pipeline', now())
on conflict(pipeline_name) do update
set last_loaded_date = excluded.last_loaded_date