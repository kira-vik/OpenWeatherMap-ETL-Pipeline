import os
import requests
from dotenv import load_dotenv
from utils import setup_logger

load_dotenv()
logger = setup_logger()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city_name):
    try:
        params = {"q": city_name, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        logger.info(f"Fetched weather data for {city_name}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch weather data for {city_name}: {e}")
        return None
