from utilities.read_properties import ReadConfig
from tests.conftest import access_token
from service.api_request import APIRequest

api_request = APIRequest()

class APIClient:
    def __init__(self):
        self.base_url = ReadConfig.get_base_url()
        self.token = access_token()

        print(self.token)

    def get_booking_ids(self):
        return api_request.get_booking_ids(base_url=self.base_url, token= self.token)


