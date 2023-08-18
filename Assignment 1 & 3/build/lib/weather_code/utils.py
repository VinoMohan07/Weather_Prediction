import os
import configparser

class ConfigHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()
        script_path = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(script_path, 'config.ini')
        self.config.read(config_file_path)

    def get_log_file_path(self):
        logs_folder = self.config.get('LOG', 'logs_folder')
        log_file_path = os.path.join(logs_folder, "logfile.log")
        return log_file_path
    
    def get_api_link(self):
        api_link = self.config.get('API', 'api_link')
        return api_link
    

confighandler=ConfigHandler()


    
