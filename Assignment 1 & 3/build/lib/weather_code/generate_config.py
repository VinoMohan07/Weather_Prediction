import configparser
import os

def generate_config_ini():
    config = configparser.ConfigParser()

    # Set API section
    config['API'] = {
        'api_link': 'https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m,relativehumidity_2m,rain,showers,snowfall,visibility,windspeed_80m'
    }

    # Set LOG section
    config['LOG'] = {
        'logs_folder': r'C:\Users\DELL\OneDrive\Documents\Vino_WIP\Weather_Prediction\logs'
    }

    # Set DATA section
    config['DATA'] = {
        'data_file_path': r'C:\Users\DELL\OneDrive\Documents\Vino_WIP\Weather_Prediction\data'
    }

    # Set test section
    config['test'] = {
        'mytest': 'sampledate'
    }

    # Get the path of the current script file
    script_path = os.path.dirname(os.path.abspath(__file__))

    # Generate the config.ini file in the same directory as the script
    config_file_path = os.path.join(script_path, 'config.ini')

    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    generate_config_ini()