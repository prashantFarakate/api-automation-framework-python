import json
import pytest
from utilities.custom_logger import LogGen
logger = LogGen()
from service.api_client import APIClient
api_client = APIClient()
from jsonschema import validate
import jsonschema.exceptions

class TestRestfulBookerAPI:
    logger = LogGen.restful_booker_api_logs()
    def test_get_booking_ids(self):
        self.logger.info(" --- Test Case 1 ---")
        self.logger.info(f" --- GET - all booking ids ---")

        response = api_client.get_booking_ids()
        assert response.status_code == 200
        self.logger.info("Test execution completed")

    def test_get_booking_by_id(self):
        self.logger.info(f" --- Test Case 2 ---")
        self.logger.info(f" --- GET - booking by id ---")

        ids = api_client.get_booking_ids()
        id = ids.as_dict[0]["bookingid"]
        response = api_client.get_booking_by_id(id=id)
        assert response.status_code == 200
        self.logger.info("Test execution completed")

    def test_get_booking_by_id_json_schema(self):
        self.logger.info(f" --- Test Case 4 ---")
        self.logger.info(f" --- GET - Validate Get Booking By ID JSON Schema ---")

        ids = api_client.get_booking_ids()
        id = ids.as_dict[0]["bookingid"]
        response = api_client.get_booking_by_id(id=id)
        assert response.status_code == 200
        with open("test_data/getBooking_schema.json", "r") as schema_file:
            schema = json.load(schema_file)
        try:
            validate(instance=response.as_dict, schema=schema)
        except jsonschema.exceptions.ValidationError as e:
            pytest.fail(f"Schema Mismatched{e}")
        self.logger.info("Test execution completed")

    def test_successful_booking_creation(self):
        self.logger.info(f" --- Test Case 3 ---")
        self.logger.info(f" --- POST : Create Booking  ---")

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
        self.logger.info("Test execution completed")

    def test_update_booking(self):
        self.logger.info(f" --- Test Case 5 ---")
        self.logger.info(f" --- PUT: Update Booking  ---")

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
        assert response.as_dict["lastname"] == "Khot"
        assert response.as_dict["totalprice"] == 1200
        assert response.as_dict["depositpaid"] == True
        assert response.as_dict["additionalneeds"] == "Lunch"
        self.logger.info("Test execution completed")

    def test_partial_update_booking(self):
        self.logger.info(f" --- Test Case 6 ---")
        self.logger.info(f" --- PATCH: Partial Update Booking ---")

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
        self.logger.info("Test execution completed")

    def test_delete_booking(self):
        self.logger.info(f" --- Test Case 6 ---")
        self.logger.info(f" --- DELETE: Delete Booking ---")

        ids = api_client.get_booking_ids()
        id = ids.as_dict[0]["bookingid"]
        response = api_client.delete_booking(id=id)
        assert response.status_code == 201
        self.logger.info("Test execution completed")


