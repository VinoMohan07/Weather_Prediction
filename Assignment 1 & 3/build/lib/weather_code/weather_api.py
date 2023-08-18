import requests
import logger

def get_weather(api_link):
    try:
        response = requests.get(api_link)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        logger.logging.error(f"Error occurred: {e}")
        return None

# def save_to_mongodb(mongo_client, database_name, collection_name, data):
#     db = mongo_client[database_name]
#     collection = db[collection_name]
#     collection.insert_one(data)