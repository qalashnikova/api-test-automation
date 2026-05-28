import requests
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tests.config import REQRES_BASE_URL, REQRES_API_KEY

HEADERS = {
    "x-api-key": REQRES_API_KEY,
    "Content-Type": "application/json"
}


class TestRegisterSuccessful:
    def test_status_code_is_200(self):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(f"{REQRES_BASE_URL}/register", json=payload, headers=HEADERS)
        assert response.status_code == 200

    def test_response_contains_id(self):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(f"{REQRES_BASE_URL}/register", json=payload, headers=HEADERS)
        body = response.json()
        assert "id" in body

    def test_response_contains_token(self):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(f"{REQRES_BASE_URL}/register", json=payload, headers=HEADERS)
        body = response.json()
        assert "token" in body

    def test_content_type_is_json(self):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(f"{REQRES_BASE_URL}/register", json=payload, headers=HEADERS)
        assert "application/json" in response.headers["Content-Type"]


class TestRegisterUnsuccessful:
    def test_status_code_is_400(self):
        payload = {"email": "sydney@fife"}
        response = requests.post(f"{REQRES_BASE_URL}/register", json=payload, headers=HEADERS)
        assert response.status_code == 400

    def test_response_contains_error_field(self):
        payload = {"email": "sydney@fife"}
        response = requests.post(f"{REQRES_BASE_URL}/register", json=payload, headers=HEADERS)
        body = response.json()
        assert "error" in body

    def test_error_is_not_empty(self):
        payload = {"email": "sydney@fife"}
        response = requests.post(f"{REQRES_BASE_URL}/register", json=payload, headers=HEADERS)
        body = response.json()
        assert len(body["error"]) > 0
