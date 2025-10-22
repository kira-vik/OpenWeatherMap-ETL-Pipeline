from sqlalchemy import text
from config import engine
from utils import setup_logger

logger = setup_logger()


def get_cities():
    query = text("SELECT city_id, city FROM cities;")
    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            cities = result.fetchall()
            logger.info(f"Fetched {len(cities)} cities from database.")
            return cities
    except Exception as e:
        logger.error(f"Failed to fetch cities: {e}")
        return []


def insert_weather_data(weather_data):
    insert_stmt = text(
        """
        INSERT INTO weather_data (
            city_id, temperature, humidity, pressure, wind_speed, cloudiness, weather_description, recorded_at
        )
        VALUES (
            :city_id, :temperature, :humidity, :pressure, :wind_speed, :cloudiness, :weather_description, NOW()
        );
    """
    )
    try:
        with engine.begin() as conn:
            conn.execute(insert_stmt, weather_data)
        logger.info(f"Inserted {len(weather_data)} weather records successfully.")
    except Exception as e:
        logger.error(f"Failed to insert weather data: {e}")
