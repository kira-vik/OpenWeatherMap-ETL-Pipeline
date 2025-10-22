import time
from services import get_cities, fetch_weather_data, insert_weather_data
from utils import setup_logger

logger = setup_logger()


def etl_process():
    cities = get_cities()

    if not cities:
        logger.warning("No cities found. Exiting ETL process.")
        return

    weather_data = []

    for city in cities:
        city_id, city_name = city

        city_weather = fetch_weather_data(city_name)

        if city_weather:
            record = {
                "city_id": city_id,
                "temperature": city_weather["main"]["temp"],
                "humidity": city_weather["main"]["humidity"],
                "pressure": city_weather["main"]["pressure"],
                "wind_speed": city_weather["wind"]["speed"],
                "cloudiness": city_weather["clouds"]["all"],
                "weather_description": city_weather["weather"][0]["description"],
            }

            weather_data.append(record)

        time.sleep(1)  # API rate limiting

    logger.info(
        f"Collected weather data for {len(weather_data)} cities: {weather_data}"
    )

    if weather_data:
        insert_weather_data(weather_data)
    else:
        logger.warning("No weather data collected to insert.")


if __name__ == "__main__":
    logger.info("Starting Weather ETL process...")
    etl_process()
    logger.info("ETL process completed")
