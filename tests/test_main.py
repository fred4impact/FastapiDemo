import requests
import pytest

@pytest.fixture
def base_url():
    return "http://localhost:8000"

def test_get_all_universities(base_url):
    # Send a GET request to the /universities endpoint
    response = requests.get(f"{base_url}/universities")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains JSON data
    assert response.headers["Content-Type"] == "application/json"

    # Check if the response contains the expected data
    expected_data = {
        1: {"name": "University A", "country": "Country A"},
        2: {"name": "University B", "country": "Country B"}
        # Add more expected data as needed
    }
    assert response.json() == expected_data