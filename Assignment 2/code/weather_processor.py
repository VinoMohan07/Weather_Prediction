import sys
import logging
from logger import LogHandler
from weather_api import WeatherDataProcessor
import pymongo
from utils import ConfigManager
from exception import CustomException

class WeatherProcessorApp:
    def __init__(self, config_manager, log_handler,latitude, longitude):
        self.config_manager = config_manager
        self.log_handler = log_handler
        self.latitude=latitude
        self.longitude=longitude

        self.api_baseurl = self.config_manager.get_api_file_path()
        self.mongodb_uri, self.database_name, self.collection_name = self.config_manager.get_MongoDB_info()
        self.data_path = self.config_manager.get_data_file_path()

        self.mongo_client = pymongo.MongoClient(self.mongodb_uri)
        self.weather_data_api = WeatherDataProcessor(self.api_baseurl, self.mongo_client, self.database_name, self.collection_name)

    def get_weather_save_db(self):
        try:

            # Get weather data from the API
            weather_data = self.weather_data_api.get_weather(self.latitude, self.longitude)

            if weather_data:
                # Save data to MongoDB
                self.weather_data_api.save_to_mongodb(weather_data)
                # Log a success message
                logging.info("Weather data saved to MongoDB.")

                # Save data to json format
                self.weather_data_api.save_json_response(weather_data,self.data_path)
                logging.info("Weather Data saved as json format")
            else:
                 # Log a failure message
                logging.warning("Weather data not available.")


        except Exception as e:
            logging.info("An error occurred while processing weather data.")
            raise CustomException(e,sys)    

