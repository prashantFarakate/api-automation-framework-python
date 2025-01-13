import logging

class LogGen:
    @staticmethod
    def restful_booker_api_logs():
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
        handler = logging.FileHandler(filename=r"C:\Users\pfarakate\OneDrive - Infor\Frameworks\Demo_Framework\api-automation-framework-python\logs\restful_booker_api.log")
        handler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger