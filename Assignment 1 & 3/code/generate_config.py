import configparser
import os

def generate_config_ini():
    config = configparser.ConfigParser()

    # Set API section
    config['API'] = {
        'api_link':'https://archive-api.open-meteo.com/v1/archive?start_date=2022-01-01&end_date=2023-08-05&hourly=temperature_2m,relativehumidity_2m,precipitation,weathercode,windspeed_10m,winddirection_10m'
       
    }

    # Set LOG section
    config['LOG'] = {
        'logs_folder': r'C:\Users\DELL\OneDrive\Documents\Vino_WIP\Weather_Prediction\logs'
    }

    # Set DATA section
    config['DATA'] = {
        'data_file_path': r'C:\Users\DELL\OneDrive\Documents\Vino_WIP\Weather_Prediction\data'
    }

    # Set Mongodb section
    config['MONGODB'] = {
        'mongodb_uri': 'mongodb+srv://mongo:mongo@cluster0.484pvm5.mongodb.net/?retryWrites=true&w=majority',
        'database_name':'Weather',
        'collection_name':'Weather_history'

    }

    # Set Login Authentication
    config['Authentication'] = {
        'username': 'User',
        'password':'abc123',
       

    }




    # Get the path of the current script file
    script_path = os.path.dirname(os.path.abspath(__file__))

    # Generate the config.ini file in the same directory as the script
    config_file_path = os.path.join(script_path, 'config.ini')

    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    generate_config_ini()