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
            return str(data)  # Convert ObjectId to string
        else:
            return data

    def save_json_response(self, data, file_path):
        data_serializable = self.convert_to_serializable(data)  # Convert MongoDB-specific types
        with open(file_path, "w") as json_file:
            json.dump(data_serializable, json_file, indent=4)   

    def add_weather_condition(self, latitude, longitude, condition):
        db = self.mongo_client[self.database_name]
        collection = db[self.collection_name]
    
        new_document = {
            'latitude': latitude,
            'longitude': longitude,
            'weather_condition': condition
        }
             
        insert_result = collection.insert_one(new_document)
           
        if insert_result.acknowledged:
            inserted_id = insert_result.inserted_id
            logging.info(f"Inserted document with ID: {inserted_id}")
            return f"Document added with ID: {inserted_id}"
        else:
            return "Insert operation not acknowledged."

    def remove_weather_condition(self):
        db = self.mongo_client[self.database_name]
        collection = db[self.collection_name]
        latitude_to_delete = 22.3511148 
        longitude_to_delete = 78.6677428

        # Specify the criteria to find the documents to delete
        query = {'latitude': latitude_to_delete, 'longitude': longitude_to_delete}
        
        # Delete all documents that match the criteria
        delete_result = collection.delete_one(query)
        print('Deleted Documents from MongoDB')
             
      


   
 

    
    
       


  


