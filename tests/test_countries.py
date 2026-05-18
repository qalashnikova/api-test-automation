import requests

BASE_URL = "https://restcountries.com/v3.1"


class TestGetCountryByCode:
    def test_status_code(self):
        response = requests.get(f"{BASE_URL}/alpha/th")
        assert response.status_code == 200

    def test_request_body(self):
        response = requests.get(f"{BASE_URL}/alpha/th")
        assert len(response.json()) > 0

    def test_single_country_returned(self):
        response = requests.get(f"{BASE_URL}/alpha/th")
        assert len(response.json()) == 1

    def test_name(self):
        response = requests.get(f"{BASE_URL}/alpha/th")
        data = response.json()
        assert data[0]["name"]["common"] == "Thailand"


class TestGetCountryByName:
    def test_status_code(self):
        response = requests.get(f"{BASE_URL}/name/thailand")
        assert response.status_code == 200

    def test_request_body(self):
        response = requests.get(f"{BASE_URL}/name/thailand")
        assert len(response.json()) > 0

    def test_single_country_returned(self):
        response = requests.get(f"{BASE_URL}/name/thailand")
        assert len(response.json()) == 1

    def test_name(self):
        response = requests.get(f"{BASE_URL}/name/thailand")
        data = response.json()
        assert data[0]["name"]["common"] == "Thailand"
