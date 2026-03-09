

def is_valid_record(record):
    if record.temperature is None:
        return False
    
    if record.temperature < -100 or record.temperature > 60:
        return False
    
    if record.wind_speed < 0 or record.wind_speed > 150:
        return False
    
    if record.precipitation < 0:
        return False