from service.api_client import APIClient
api_client = APIClient()

def test_get_booking_ids():
    response = api_client.get_booking_ids()
    assert response.status_code == 200

