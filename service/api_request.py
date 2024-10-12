import requests
from dataclasses import dataclass

@dataclass
class APIResponse:
    status_code : str
    text : str
    as_dict : object
    headers : dict

class APIRequest:
    '''
            GET , POST , PUT , DELETE and collect all resp
    '''

    def get_response(self, response):
        status_code = response.status_code
        text = response.text
        headers = response.headers
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        return APIResponse(status_code, text, as_dict, headers)

    # GET
    def get_booking_ids(self, base_url, token):
        url = f"{base_url}/booking"
        headers = {
            "Content-Type": "application/json",
            "Authorization": token
            }

        response = requests.request("GET", url=url, headers=headers)
        return self.get_response(response)




