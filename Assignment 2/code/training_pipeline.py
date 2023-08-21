import os
import sys
import pandas as pd
import logging

from data_ingestion import DataIngestion
from data_transformation import DataTransformation
from model_trainer import ModelTrainer
from exception import CustomException
from logger import LogHandler
from utils import ConfigManager




if __name__=='__main__':
     # To handle logging
    log_handler = LogHandler()
    log_handler.setup_logging()
    # To read the datas from config.ini
    config_manager = ConfigManager()

    # Model Training
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion(config_manager)  
    data_transformation=DataTransformation()  
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)  
    model_trainer=ModelTrainer()
    model_trainer.initiate_model_training(train_arr, test_arr)  



    