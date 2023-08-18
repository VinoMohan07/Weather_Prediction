import os
import sys
import pandas as pd
import numpy as np
import logging
from math import sqrt

from data_ingestion import DataIngestion
from data_transformation import DataTransformation
from logger import LogHandler
from exception import CustomException
from utils import ConfigManager,save_object,load_object

from dataclasses import dataclass
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')
    predicted_output_file_path=os.path.join('artifacts','output.csv')
    
class ModelTrainer:

    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def save_trained_model(self,model):
        save_object(self.model_trainer_config.trained_model_file_path,model)  

     

    def initiate_model_training(self,train_array, test_array):
        try:
            logging.info('Model Training Started')
            history=[x for x in train_array]
            predictions=list()
            observed=list()

            # walk-forward validation
            for t in range(len(test_array)):
                model = ARIMA(history, order=(5,1,0))
                model_fit = model.fit()
                output = model_fit.forecast()
                yhat = output[0]
                predictions.append(yhat)
                obs = test_array[t]
                history.append(obs)
                observed.append(obs)
                # print('predicted=%f, expected=%f' % (yhat, obs))

                # Create a DataFrame to store predictions
            predictions_df =pd.DataFrame({'Predicted': predictions})
            
                # Save predictions to a CSV file
            predictions_df.to_csv(self.model_trainer_config.predicted_output_file_path, index=False)
                
                
        # evaluate forecasts
            rmse = sqrt(mean_squared_error(test_array, predictions))
            logging.info('Test RMSE: %.3f' % rmse)
            print('Test RMSE: %.3f' % rmse) 

            
            # # Create a DataFrame to store predictions
            # predictions_df =pd.DataFrame({'Predicted': predictions,  'Observed': obs})
            
            # # Save predictions to a CSV file
            # predictions_df.to_csv(self.model_trainer_config.predicted_output_file_path, index=False)
         
            self.save_trained_model(model_fit)
            print("Model saved as pickle file")


            
        except Exception as e:
            logging.info('Error occurred at Model Trainer stage')
            raise CustomException(e,sys)

'''
if __name__ == "__main__":
    # To handle logging
    log_handler = LogHandler()
    log_handler.setup_logging()

    # To read the datas from config.ini
    config_manager = ConfigManager()

    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion(config_manager)
     
    data_transformation=DataTransformation()  
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path) 

    model_trainer=ModelTrainer()
    model_trainer.initiate_model_training(train_arr, test_arr) 
         
'''

