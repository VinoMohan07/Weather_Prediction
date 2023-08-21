import os
import configparser
import sys
import re
import weather_code

sys.path.insert(1,"C:\\Users\\DELL\\OneDrive\\Documents\\Vino_WIP\\Weather_Prediction\\weather_code")

# logs_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
# print(logs_folder)

#  # Read config.ini
# config = configparser.ConfigParser()
# script_path = os.path.dirname(os.path.abspath(__file__))
# print(script_path)
# config_file_path = os.path.join(script_path, 'config.ini')
# print(config_file_path)
# config.read(config_file_path)

# # Access the 'mytest' option in the 'test' section
# a = config['LOG']['logs_folder']
# print(a)



# [API]
# api_link = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m,relativehumidity_2m,rain,showers,snowfall,visibility,windspeed_80m"

# [LOG]
# logs_folder = C:\Users\DELL\OneDrive\Documents\Vino_WIP\Weather_Prediction\logs

# [DATA]
# data_file_path="C:\Users\DELL\OneDrive\Documents\Vino_WIP\Weather_Prediction\data"

# [test]
# mytest='sampledate'

# [MONGODB]
# mongodb_uri = mongodb+srv://mongo:<mongo>@cluster0.484pvm5.mongodb.net/?retryWrites=true&w=majority
# database_name = weather_db
# collection_name = weather_collection






# working


# def get_log_file_path():
#     logs_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
#     return os.path.join(logs_folder, "logfile.log")

# # Set up logging configuration
# log_file = get_log_file_path()
# logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



# logger working 
# import logging
# import configparser
# import os

# def get_log_file_path():
#     config = configparser.ConfigParser()
#     script_path = os.path.dirname(os.path.abspath(__file__))
#     config_file_path = os.path.join(script_path, 'config.ini')
#     config.read(config_file_path)
#     logs_folder = config['LOG']['logs_folder']
#     log_file_path=os.path.join(logs_folder, "logfile.log")
#     return log_file_path


# # Set up logging configuration
# log_file = get_log_file_path()
# logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.info("Log File created Sucessfully")



# from weather_code.utils import ConfigHandler
from weather_code.logger import LogHandler
