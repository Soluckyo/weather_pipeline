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
 order by fw.obs_date desc
