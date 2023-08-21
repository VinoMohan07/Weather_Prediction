from flask import Flask, request, render_template
from logger import LogHandler
from utils import ConfigManager  # To read the config file
from exception import CustomException
from weather_api import WeatherDataProcessor #To read data from the API
from weather_processor import WeatherProcessorApp  # To do the MongoDB operation
from prediction_pipeline import PredictPipeline
import pymongo
import logging

app = Flask(__name__)

# Initialize LogHandler and ConfigManager
log_handler = LogHandler()
log_handler.setup_logging()
config_manager = ConfigManager()

@app.route('/weather_forecast', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_date = request.form['input_date']  # Get input date from form
        forecast_days = int(request.form['forecast_days'])  # Get forecast days from form
        print(input_date,forecast_days)

        # Use your prediction pipeline to predict the temperature
        predict_pipeline = PredictPipeline()  # Initialize your prediction pipeline
        forecasted_temperature = predict_pipeline.predict(input_date, forecast_days)
        
        
        return render_template('index.html', forecasted_temperature=forecasted_temperature)

    return render_template('index.html', forecasted_temperature=None)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)