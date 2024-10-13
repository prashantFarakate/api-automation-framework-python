import json
import pytest
from service.api_client import APIClient
api_client = APIClient()
from jsonschema import validate
import jsonschema.exceptions

class TestRestfulBookerAPI:
    def test_get_booking_ids(self):
        response = api_client.get_booking_ids()
        print(response.as_dict)
        assert response.status_code == 200

    def test_get_booking_by_id(self):
        ids = api_client.get_booking_ids()
        id = ids.as_dict[0]["bookingid"]
        response = api_client.get_booking_by_id(id=id)
        print(response.as_dict)
        assert response.status_code == 200

    def test_get_booking_by_id_json_schema(self):
        response = api_client.get_booking_by_id(id=1)
        assert response.status_code == 200
        with open("test_data/getBooking_schema.json", "r") as schema_file:
            schema = json.load(schema_file)
        try:
            validate(instance=response.as_dict, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            pytest.fail(f"Schema Mismatched{e}")

    def test_successful_booking_creation(self):
        booking_data = {
            "firstname": "Prashant",
            "lastname": "Farakate",
            "totalprice": 100,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-05"
            },
            "additionalneeds": "Dinner"
        }

        response = api_client.create_booking(booking_data)
        assert response.status_code == 200
        assert response.as_dict["booking"]["firstname"] == "Prashant"
        assert response.as_dict["booking"]["lastname"] == "Farakate"
        assert response.as_dict["booking"]["additionalneeds"] == "Dinner"

    def test_update_booking(self):
        ids = api_client.get_booking_ids()
        id = ids.as_dict[0]["bookingid"]

        updated_data = {
            "firstname": "Sachin",
            "lastname": "Khot",
            "totalprice": 1200,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-05"
            },
            "additionalneeds": "Lunch"
        }
        response = api_client.update_booking(id, updated_data)

        assert response.status_code == 200
        assert response.as_dict["firstname"] == "Sachin"
        assert response.as_dict["lastname"] == "khot"
        assert response.as_dict["totalprice"] == 1200
        assert response.as_dict["depositpaid"] == True
        assert response.as_dict["additionalneeds"] == "Lunch"

    def test_partial_update_booking(self):
        ids = api_client.get_booking_ids()
        id = ids.as_dict[0]["bookingid"]

        partially_updated_data = {
            "totalprice": 2400,
            "additionalneeds": "Dinner"
        }
        response = api_client.partial_update_booking(id, partially_updated_data)

        assert response.status_code == 200
        assert response.as_dict["totalprice"] == 2400
        assert response.as_dict["additionalneeds"] == "Dinner"

    def test_delete_booking(self):
        ids = api_client.get_booking_ids()
        id = ids.as_dict[0]["bookingid"]
        response = api_client.delete_booking(id=id)
        assert response.status_code == 201


