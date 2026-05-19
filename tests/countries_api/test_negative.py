import requests
import pytest
from config import BASE_URL


class TestInvalidCountry:

    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/name/utopia")

    def test_status_code(self, response):
        assert response.status_code == 404

    def test_message(self, response):
        data = response.json()
        assert data["message"] == "Not Found"


class TestInvalidCode:
    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/alpha/wat")

    def test_status_code(self, response):
        assert response.status_code == 404

    def test_message(self, response):
        data = response.json()
        assert data["message"] == "Not Found"


class TestInvalidCurrency:
    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/currency/auf")

    def test_status_code(self, response):
        assert response.status_code == 404

    def test_message(self, response):
        data = response.json()
        assert data["message"] == "Not Found"


class TestInvalidRegion:
    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/region/mars")

    def test_status_code(self, response):
        assert response.status_code == 404

    def test_message(self, response):
        data = response.json()
        assert data["message"] == "Not Found"


class TestInvalidLanguage:
    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/lang/elf")

    def test_status_code(self, response):
        assert response.status_code == 404

    def test_message(self, response):
        data = response.json()
        assert data["message"] == "Not Found"
