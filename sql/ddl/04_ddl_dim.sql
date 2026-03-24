--создание таблицы городов
create table dim_city(
city_id serial primary key,
city_name text unique,
created_at timestamp default now())