import os
import sys
import logging

# from exception import CustomException
from logger import LogHandler
from utils import ConfigManager,save_object,load_object
import pandas as pd
from model_trainer import ModelTrainer

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, input_date, forecast_days):
        try:
            # Convert input date to datetime format
            input_date_dt = pd.to_datetime(input_date, format='%Y-%m-%d')

            # Load trained model
            model_path = os.path.join('artifacts', 'model.pkl')
            model = load_object(model_path)
          
            forecast_range = pd.date_range(start=input_date_dt, periods=forecast_days, freq='D')
            forecasted_temperature = model.forecast(steps=len(forecast_range))
            # print(forecasted_temperature)

            return forecasted_temperature.tolist()
            logging.info("Prediction completed")

        except Exception as e:
            logging.info("Error Occurred at Predict Pipeline")
            # raise CustomException(e, sys)



