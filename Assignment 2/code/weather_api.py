import requests
import logging
from logger import LogHandler
from exception import CustomException
import json
from bson import ObjectId

loghandler=LogHandler()
loghandler.setup_logging()



class WeatherDataProcessor:
    def __init__(self, api_baseurl, mongo_client, database_name, collection_name):
        self.api_baseurl = api_baseurl
        self.mongo_client = mongo_client
        self.database_name = database_name
        self.collection_name = collection_name

    def get_weather(self,latitude, longitude):
        api_link = f"{self.api_baseurl}&latitude={latitude}&longitude={longitude}"
        
        try:
            response = requests.get(api_link)
            response.raise_for_status()
            weather_data = response.json()
            logging.info("Got weather data from the API")
            return weather_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error occurred: {e}")
            return None

    def is_valid_document(self, document):
        return isinstance(document, dict)

    def save_to_mongodb(self, data):
        db = self.mongo_client[self.database_name]
        collection = db[self.collection_name]
        collection.insert_one(data)

    def convert_to_serializable(self, data):
        if isinstance(data, list):
            return [self.convert_to_serializable(item) for item in data]
        elif isinstance(data, dict):
            return {key: self.convert_to_serializable(value) for key, value in data.items()}
        elif isinstance(data, ObjectId):
            return str(data)
        else:
            return data

    def save_json_response(self, data, file_path):
        data_serializable = self.convert_to_serializable(data)
        with open(file_path, "w") as json_file:
            json.dump(data_serializable, json_file, indent=4)    

   


