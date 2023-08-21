
import os
import pandas as pd
import numpy as np
import sys
import logging
import json
from utils import ConfigManager
from logger import LogHandler
from exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#Data class is a class that store the data, it doesnt have any methods


# Initialize the Data Ingestion config
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts', 'train.csv')
    test_data_path:str=os.path.join('artifacts', 'test.csv')
    raw_data_path:str=os.path.join('artifacts', 'raw.json')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()
        


    def initiate_data_ingestion(self,config_manager):
        logging.info('Data Ingestion Method Starts')
        try:
             #  Use config_manager instance to get data file path
            source_file_path=config_manager.get_data_file_path()
           
            with open(source_file_path, "r") as json_file:
                json_content = json_file.read()

            json_data = json.loads(json_content)
            hourly_data=json_data['hourly']
            logging.info('Extracted Hourly datas from the json file')

            df = pd.DataFrame(hourly_data)
            logging.info('Dataset read as Pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_json(self.ingestion_config.raw_data_path, orient='records')
            logging.info('Raw Data Saved as JSON file')

            logging.info('Train Test Split')
            # Assuming you have a DataFrame named df with a datetime index
            total_data_points = len(df)
            train_ratio = 0.80  # Specify the proportion for training data

            split_index = int(total_data_points * train_ratio)
            train_set = df[:split_index]
            test_set = df[split_index:]

            train_set.to_csv(self.ingestion_config.train_data_path)
            test_set.to_csv(self.ingestion_config.test_data_path)
            
            logging.info('DataIngestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        except Exception as e:
            logging.info('Error Occured at DataIngestion stage')    
            raise CustomException(e,sys)

