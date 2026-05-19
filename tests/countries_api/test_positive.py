import requests
import pytest
from config import BASE_URL


def get_country_names(countries):
    return [country["name"]["common"] for country in countries]


@pytest.mark.parametrize(
    "url",
    [
        "/alpha/th",
        "/name/thailand",
        "/region/asia",
        "/currency/rub",
        "/lang/english",
        "/all?fields=name,capital,region",
    ],
)
def test_valid_status_body(url):
    response = requests.get(f"{BASE_URL}{url}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


class TestGetCountryByCode:

    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/alpha/th")

    def test_single_country_returned(self, response):
        data = response.json()
        assert len(data) == 1

    def test_name(self, response):
        data = response.json()
        assert data[0]["name"]["common"] == "Thailand"


class TestGetCountryByName:

    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/name/thailand")

    def test_single_country_returned(self, response):
        assert len(response.json()) == 1

    def test_name(self, response):
        data = response.json()
        assert data[0]["name"]["common"] == "Thailand"


class TestGetByRegion:

    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/region/asia")

    def test_asian_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "Thailand" in names

    def test_non_asian_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "Spain" not in names


class TestGetByCurrency:

    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/currency/rub")

    def test_currency(self, response):
        data = response.json()
        russia = next(
            country for country in data if country["name"]["common"] == "Russia"
        )
        assert russia["currencies"]["RUB"]["name"] == "Russian ruble"

    def test_rub_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "Russia" in names

    def test_non_rub_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "Thailand" not in names


class TestGetByLanguage:

    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/lang/english")

    def test_language(self, response):
        data = response.json()
        assert "English" in data[0]["languages"].values()

    def test_eng_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "United States" in names

    def test_non_eng_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "Russia" not in names


class TestAllCountries:

    @pytest.fixture
    def response(self):
        return requests.get(f"{BASE_URL}/all?fields=name,capital,region")

    def test_multiple_country_returned(self, response):
        assert len(response.json()) > 1

    def test_no_currencies(self, response):
        data = response.json()
        assert "currencies" not in data[0]

    def test_no_languages(self, response):
        data = response.json()
        assert "languages" not in data[0]

    def test_real_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "United States" in names

    def test_not_real_country(self, response):
        data = response.json()
        names = get_country_names(data)
        assert "Utopia" not in names
