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