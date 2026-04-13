--создание таблицы городов
\connect weather;

CREATE TABLE IF NOT EXISTS dim_city(
city_id serial primary key,
city_name text unique,
created_at timestamp default now())