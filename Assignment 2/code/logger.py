
import logging
import configparser
import os


class LogHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()
        script_path = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_path, 'config.ini')
        self.config.read(config_file_path)

    def get_log_file_path(self):
        logs_folder = self.config.get('LOG', 'logs_folder')
        log_file_path = os.path.join(logs_folder, "logfile.log")
        return log_file_path

    def setup_logging(self):
        log_file = self.get_log_file_path()
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Log File created Successfully")


    