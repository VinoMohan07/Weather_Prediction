import pandas as pd
import numpy as np
import os
import sys
import logging
from datetime import datetime
from exception import CustomException
from logger import LogHandler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from data_ingestion import DataIngestion
from utils import ConfigManager,save_object,load_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation: 

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    

    def save_preprocessor(self):
        save_object(self.data_transformation_config.preprocessor_obj_file_path, self)
    

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            #read train and test data from the path
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train data head: \n{train_df.head().to_string()}')
            logging.info(f'Test data head: \n{test_df.head().to_string()}')

            # Selecting only the required columns
            selected_columns = ['time', 'temperature_2m']
            target_columns='temperature_2m'
            input_feature_train_df = train_df[selected_columns]
            input_feature_test_df = test_df[selected_columns]
           

            # Converting time column to datetime format and setting as index
            time_column_name = 'time'  
            input_feature_train_df.loc[:, time_column_name] = pd.to_datetime(input_feature_train_df[time_column_name], format='%Y-%m-%dT%H:%M')
            input_feature_test_df.loc[:, time_column_name] = pd.to_datetime(input_feature_test_df[time_column_name], format='%Y-%m-%dT%H:%M')
            
            
            input_feature_train_df.set_index(time_column_name, inplace=True)
            input_feature_test_df.set_index(time_column_name, inplace=True)

            logging.info("Set Timestamp as Index successfully")

            # Perform imputation using the median strategy
            imputer = SimpleImputer(strategy='median')
            input_feature_train_df_transformed = imputer.fit_transform(input_feature_train_df)
            input_feature_test_df_transformed = imputer.transform(input_feature_test_df)
            logging.info("Simple Imputation completed")

            # Convert the transformed arrays back to DataFrames
            input_feature_train_df_transformed = pd.DataFrame(input_feature_train_df_transformed, columns=input_feature_train_df.columns, index=input_feature_train_df.index)
            input_feature_test_df_transformed = pd.DataFrame(input_feature_test_df_transformed, columns=input_feature_test_df.columns, index=input_feature_test_df.index)

                              
            # Resample the transformed DataFrames
            input_feature_train_df_resampled = input_feature_train_df_transformed['temperature_2m'].resample('D').mean()
            input_feature_test_df_resampled = input_feature_test_df_transformed['temperature_2m'].resample('D').mean()
            logging.info("Converted Hourly Datas to Daily Datas")

            
            logging.info('Read Resampled train and test data completed')
            logging.info(f'Train data head: \n{input_feature_train_df_resampled.head().to_string()}')
            logging.info(f'Test data head: \n{input_feature_test_df_resampled.head().to_string()}')

            # Convert the resampled DataFrames to NumPy arrays
            input_feature_train_arr = input_feature_train_df_resampled.values
            input_feature_test_arr = input_feature_test_df_resampled.values

            #Save the preprocessing steps as pickle file
            self.save_preprocessor()

            logging.info("Preprocessing Done!! Saved as Pickled File")
            logging.info(input_feature_train_arr)

            return (
                input_feature_train_arr,
                input_feature_test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.info("Error occured at the DataTransformation stage")
            raise CustomException (e,sys)
        



      




        