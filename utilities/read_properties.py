import configparser
# import os

config =configparser.ConfigParser()
# config.read("configurations/config.ini")
config.read(r"C:\Users\pfarakate\OneDrive - Infor\Frameworks\Demo_Framework\api-automation-framework-python\configurations\config.ini")
# config_path = os.path.join(os.path.dirname(__file__), "configurations/config.ini")
# config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get("restfulBooker", "base_url")


# import os
# import configparser
#
# class ReadConfig:
#     @staticmethod
#     def get_base_url():
#         config = configparser.ConfigParser()
#         # Dynamically get the absolute path of config.ini
#         config_path = os.path.join(os.path.dirname(__file__), '../config.ini')
#         if not os.path.exists(config_path):
#             raise FileNotFoundError(f"Configuration file not found at {config_path}")
#         config.read(config_path)
#         if "restfulBooker" not in config:
#             raise KeyError(f"'restfulBooker' section not found in {config_path}")
#         return config.get("restfulBooker", "base_url")

# import os
# import configparser
#
#
# class ReadConfig:
#     @staticmethod
#     def get_base_url():
#         config = configparser.ConfigParser()
#
#         # Dynamically get the absolute path of config.ini
#         config_path = os.path.join(os.path.dirname(__file__), '../config.ini')
#
#         # Check if the config file exists
#         if not os.path.exists(config_path):
#             raise FileNotFoundError(f"Configuration file not found at {config_path}")
#
#         # Read the config file
#         config.read(config_path)
#
#         # Verify the section exists
#         if "restfulBooker" not in config:
#             raise KeyError(f"'restfulBooker' section not found in {config_path}")
#
#         # Get the base_url value
#         try:
#             base_url = config.get("restfulBooker", "base_url")
#         except configparser.NoOptionError:
#             raise KeyError(f"'base_url' option not found in 'restfulBooker' section of {config_path}")
#
#         return base_url
