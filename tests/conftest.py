import requests

base_url = "https://restful-booker.herokuapp.com"

def access_token():
    url = f"{base_url}/auth"
    headers = {"Content-Type": "application/json"}
    data = {"username": "admin", "password": "password123"}

    response = requests.request("POST", url=url, headers=headers, json=data)
    token = response.json()["token"]
    return token








