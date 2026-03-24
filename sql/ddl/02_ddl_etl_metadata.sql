CREATE TABLE IF NOT EXISTS etl_metadata(
    pipeline_name TEXT PRIMARY KEY,
    last_loaded_date DATE
);