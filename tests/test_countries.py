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


class TestInvalidCountry:
    def test_status_code(self):
        response = requests.get(f"{BASE_URL}/name/utopia")
        assert response.status_code == 404

    def test_message(self):
        response = requests.get(f"{BASE_URL}/name/utopia")
        data = response.json()
        assert data["message"] == "Not Found"


class TestGetByRegion:
    def test_status_code(self):
        response = requests.get(f"{BASE_URL}/region/asia")
        assert response.status_code == 200

    def test_request_body(self):
        response = requests.get(f"{BASE_URL}/region/asia")
        assert len(response.json()) > 0

    def test_asian_country(self):
        response = requests.get(f"{BASE_URL}/region/asia")
        data = response.json()
        names = [country["name"]["common"] for country in data]
        assert "Thailand" in names

    def test_non_asian_country(self):
        response = requests.get(f"{BASE_URL}/region/asia")
        data = response.json()
        names = [country["name"]["common"] for country in data]
        assert "Spain" not in names


class TestGetByCurrency:
    def test_status_code(self):
        response = requests.get(f"{BASE_URL}/currency/rub")
        assert response.status_code == 200

    def test_request_body(self):
        response = requests.get(f"{BASE_URL}/currency/rub")
        assert len(response.json()) > 0

    def test_currency(self):
        response = requests.get(f"{BASE_URL}/currency/rub")
        data = response.json()
        # to do: refactor with next()
        russia = None
        for country in data:
            if country["name"]["common"] == "Russia":
                russia = country
        assert russia["currencies"]["RUB"]["name"] == "Russian ruble"

    def test_rub_country(self):
        response = requests.get(f"{BASE_URL}/currency/rub")
        data = response.json()
        names = [country["name"]["common"] for country in data]
        assert "Russia" in names

    def test_non_rub_country(self):
        response = requests.get(f"{BASE_URL}/currency/rub")
        data = response.json()
        names = [country["name"]["common"] for country in data]
        assert "Thailand" not in names


class TestGetByLanguage:
    def test_status_code(self):
        response = requests.get(f"{BASE_URL}/lang/english")
        assert response.status_code == 200

    def test_request_body(self):
        response = requests.get(f"{BASE_URL}/lang/english")
        assert len(response.json()) > 0

    def test_language(self):
        response = requests.get(f"{BASE_URL}/lang/english")
        data = response.json()
        assert "English" in data[0]["languages"].values()

    def test_eng_country(self):
        response = requests.get(f"{BASE_URL}/lang/english")
        data = response.json()
        names = [country["name"]["common"] for country in data]
        assert "United States" in names

    def test_non_eng_country(self):
        response = requests.get(f"{BASE_URL}/lang/english")
        data = response.json()
        names = [country["name"]["common"] for country in data]
        assert "Russia" not in names
