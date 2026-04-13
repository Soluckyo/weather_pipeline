from logger import get_logger

logger = get_logger(__name__)

def is_valid_record(record):
    if record.temperature is None:
        logger.warning(f"Invalid temp (null): {record}")
        return False
    
    if record.temperature < -100 or record.temperature > 60:
        logger.warning(f"Invalid temp: {record}")
        return False
    
    if record.wind_speed < 0 or record.wind_speed > 150:
        logger.warning(f"Invalid wind: {record}")
        return False
    
    if record.precipitation < 0:
        logger.warning(f"Invalid precip: {record}")
        return False
    
    return True