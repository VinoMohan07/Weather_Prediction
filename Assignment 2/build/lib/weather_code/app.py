import configparser
from weather_code.logger import LogHandler
from weather_code.weather_api import get_weather, save_to_mongodb
import pymongo

def get_weather_save_db():
    # Read configuration from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_link = config['API']['api_link']
    mongodb_uri = config['MONGODB']['mongodb_uri']
    database_name = config['MONGODB']['database_name']
    collection_name = config['MONGODB']['collection_name']

    # MongoDB configuration
    mongo_client = pymongo.MongoClient(mongodb_uri)

    # Get weather data from the API
    weather_data = get_weather(api_link)

    if weather_data:
        # Save data to MongoDB
        save_to_mongodb(mongo_client, database_name, collection_name, weather_data)

        # Log a success message
        logger.logging.info("Weather data saved to MongoDB.")
    else:
        # Log a failure message
        logger.logging.warning("Weather data not available.")


if __name__ == "__main__":
    get_weather_save_db()