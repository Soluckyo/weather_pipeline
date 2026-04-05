--load mart_city_stats
truncate table mart_city_stats;	
	
insert into mart_city_stats
select dc.city_name as city_name,
	   round(avg(fw.temperature)::numeric, 2) as avg_temp,
	   min(fw.temperature) as min_temp,
	   max(fw.temperature) as max_temp,
	   round(avg(fw.wind_speed)::numeric, 2) as avg_wind_speed,
	   now() as load_date
  from fct_weather fw
  join dim_city dc on dc.city_id = fw.city_id
 group by dc.city_name;