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

            # Load your trained model
            model_path = os.path.join('artifacts', 'model.pkl')
            model = load_object(model_path)

            # Generate a range of dates for forecasting
            forecast_range = pd.date_range(start=input_date_dt, periods=forecast_days, freq='D')

            # Forecast using the forecast range
            forecasted_temperature = model.forecast(steps=len(forecast_range))  # Adjust this based on your model's API

            return forecasted_temperature.tolist()
            logging.info("Prediction completed")

        except Exception as e:
            logging.info("Error Occurred at Predict Pipeline")
            raise CustomException(e, sys)


'''
if __name__ == "__main__":
    log_handler = LogHandler()
    log_handler.setup_logging()

    config_manager = ConfigManager()

    input_date = '2023-08-15'  # Specify the input date in the desired format
    forecast_days = 7  # Specify the number of days to forecast

    predict_pipeline = PredictPipeline()
    forecasted_temperature = predict_pipeline.predict(input_date, forecast_days)

    print("Forecasted Temperatures:", forecasted_temperature)

'''


















































        




      

