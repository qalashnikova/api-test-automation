import requests
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from tests.config import REQRES_BASE_URL, REQRES_API_KEY

HEADERS = {"x-api-key": REQRES_API_KEY}


class TestListUsers:
    def test_status_code_is_200(self):
        response = requests.get(f"{REQRES_BASE_URL}/users", params={"page": 2}, headers=HEADERS)
        assert response.status_code == 200

    def test_response_contains_data(self):
        response = requests.get(f"{REQRES_BASE_URL}/users", params={"page": 2}, headers=HEADERS)
        body = response.json()
        assert "data" in body
        assert len(body["data"]) > 0

    def test_response_contains_pagination_fields(self):
        response = requests.get(f"{REQRES_BASE_URL}/users", params={"page": 2}, headers=HEADERS)
        body = response.json()
        assert "page" in body
        assert "total" in body
        assert "total_pages" in body

    def test_page_number_matches_request(self):
        response = requests.get(f"{REQRES_BASE_URL}/users", params={"page": 2}, headers=HEADERS)
        body = response.json()
        assert body["page"] == 2


class TestSingleUser:
    def test_status_code_is_200(self):
        response = requests.get(f"{REQRES_BASE_URL}/users/2", headers=HEADERS)
        assert response.status_code == 200

    def test_response_contains_data(self):
        response = requests.get(f"{REQRES_BASE_URL}/users/2", headers=HEADERS)
        body = response.json()
        assert "data" in body

    def test_user_has_required_fields(self):
        response = requests.get(f"{REQRES_BASE_URL}/users/2", headers=HEADERS)
        user = response.json()["data"]
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user

    def test_user_id_matches_request(self):
        response = requests.get(f"{REQRES_BASE_URL}/users/2", headers=HEADERS)
        user = response.json()["data"]
        assert user["id"] == 2


class TestCreateUser:
    def test_status_code_is_201(self):
        payload = {"name": "morpheus", "job": "leader"}
        response = requests.post(f"{REQRES_BASE_URL}/users", json=payload, headers=HEADERS)
        assert response.status_code == 201

    def test_response_contains_id(self):
        payload = {"name": "morpheus", "job": "leader"}
        response = requests.post(f"{REQRES_BASE_URL}/users", json=payload, headers=HEADERS)
        body = response.json()
        assert "id" in body

    def test_response_contains_correct_name(self):
        payload = {"name": "morpheus", "job": "leader"}
        response = requests.post(f"{REQRES_BASE_URL}/users", json=payload, headers=HEADERS)
        body = response.json()
        assert body["name"] == "morpheus"

    def test_response_contains_correct_job(self):
        payload = {"name": "morpheus", "job": "leader"}
        response = requests.post(f"{REQRES_BASE_URL}/users", json=payload, headers=HEADERS)
        body = response.json()
        assert body["job"] == "leader"


class TestUpdateUser:
    def test_put_status_code_is_200(self):
        payload = {"name": "morpheus", "job": "zion resident"}
        response = requests.put(f"{REQRES_BASE_URL}/users/2", json=payload, headers=HEADERS)
        assert response.status_code == 200

    def test_put_response_contains_updated_job(self):
        payload = {"name": "morpheus", "job": "zion resident"}
        response = requests.put(f"{REQRES_BASE_URL}/users/2", json=payload, headers=HEADERS)
        body = response.json()
        assert body["job"] == "zion resident"

    def test_patch_status_code_is_200(self):
        payload = {"name": "morpheus", "job": "zion resident"}
        response = requests.patch(f"{REQRES_BASE_URL}/users/2", json=payload, headers=HEADERS)
        assert response.status_code == 200

    def test_patch_response_contains_updated_name(self):
        payload = {"name": "morpheus", "job": "zion resident"}
        response = requests.patch(f"{REQRES_BASE_URL}/users/2", json=payload, headers=HEADERS)
        body = response.json()
        assert body["name"] == "morpheus"


class TestDeleteUser:
    def test_status_code_is_204(self):
        response = requests.delete(f"{REQRES_BASE_URL}/users/2", headers=HEADERS)
        assert response.status_code == 204

    def test_response_body_is_empty(self):
        response = requests.delete(f"{REQRES_BASE_URL}/users/2", headers=HEADERS)
        assert response.text == ""
