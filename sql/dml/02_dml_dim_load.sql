--заполнение таблицы городов
insert into dim_city(city_name)
select distinct sw.city 
  from stg_weather sw
    on conflict(city_name) do nothing;

--обновление metadata
insert into etl_metadata(pipeline_name, last_loaded_date)
values('dim_city', now())
on conflict(pipeline_name) do update
set last_loaded_date = excluded.last_loaded_date