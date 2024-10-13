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
        headers = {"Content-Type": "application/json","Authorization": token}
        response = requests.request("GET", url=url, headers=headers)
        return self.get_response(response)

    # GET
    def get_booking_by_id(self, base_url, token, id):
        url = f"{base_url}/booking/{id}"
        headers = {"Content-Type":"application/json", "Authorization":token}
        response = requests.get(url=url, headers=headers)
        return self.get_response(response)

    # POST
    def create_booking(self, base_url, token, booking_data):
        url = f"{base_url}/booking"
        headers = {"Content-Type": "application/json", "Authorization": token}
        payload = booking_data
        response = requests.post(url, headers=headers, json=payload)
        return self.get_response(response)

    # PUT
    def update_booking(self, base_url, token, id, updated_data):
        url = f"{base_url}/booking/{id}"
        headers = {
            "Content-Type" : "application/json",
            "Accept" : "application/json"
        }
        cookies = {
            "token": token
        }
        payload = updated_data
        response = requests.put(url, headers=headers, cookies=cookies, json=payload)
        return self.get_response(response)

    #Patch
    def partial_update_booking(self, base_url, token, id, partially_updated_data):
        url = f"{base_url}/booking/{id}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        cookies = {
            "token": token
        }
        payload = partially_updated_data
        response = requests.patch(url, headers=headers, cookies=cookies, json=payload)
        return self.get_response(response)

    # DELETE
    def delete_booking(self, base_url, token, id):
        url = f"{base_url}/booking/{id}"
        headers = {"Content-Type": "application/json"}
        cookies = {"token": token}
        response = requests.delete(url, headers=headers, cookies=cookies)
        return self.get_response(response)









