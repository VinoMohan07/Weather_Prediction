import os
import sys
import configparser
import logging
from exception import CustomException
import pickle
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


class ConfigManager:
    def __init__(self):
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(self.script_path, 'config.ini')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)

    def get_api_file_path(self):
        api_base_url = self.config['API']['api_link']
        return api_base_url

    def get_MongoDB_info(self):
        mongodb_uri = self.config['MONGODB']['mongodb_uri']
        database_name = self.config['MONGODB']['database_name']
        collection_name = self.config['MONGODB']['collection_name']
        return mongodb_uri, database_name, collection_name
    
    def get_data_file_path(self):
        data_folder = self.config.get('DATA', 'data_file_path')
        data_file_path = os.path.join(data_folder, "raw_data.json")
        return data_file_path
    

    def get_authentication_username(self):
        return self.config.get('Authentication', 'username')

    def get_authentication_password(self):
        return self.config.get('Authentication', 'password')


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info("Error occurred at save pickle file stage")
        raise CustomException(e,sys)        




def load_object(file_path):
    try:
        with open (file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info("Error Occured at Pickle file loading in utils")
        raise CustomException(e,sys)

    

 





