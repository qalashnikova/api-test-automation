import requests
import pytest
from config import BASE_URL


@pytest.mark.parametrize(
    "url", ["/name/utopia", "/alpha/wat", "/currency/auf", "/region/mars", "/lang/elf"]
)
def test_invalid_returns_404(url):
    response = requests.get(f"{BASE_URL}{url}")
    assert response.status_code == 404
    data = response.json()
    assert data["message"] == "Not Found"
