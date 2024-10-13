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

    def get_booking_by_id(self, id):
        return api_request.get_booking_by_id(self.base_url, self.token, id)

    def create_booking(self, booking_data):
        return api_request.create_booking(self.base_url, self.token, booking_data)

    def update_booking(self, id, updated_data):
        return api_request.update_booking(self.base_url, self.token, id, updated_data)

    def partial_update_booking(self, id, partially_updated_data):
        return api_request.partial_update_booking(self.base_url, self.token, id, partially_updated_data)

    def delete_booking(self, id):
        return api_request.delete_booking(self.base_url, self.token, id)
