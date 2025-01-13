import configparser

config =configparser.ConfigParser()
config.read("configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get("restfulBooker", "base_url")


