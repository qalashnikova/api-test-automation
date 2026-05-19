import requests
import pytest
from config import BASE_URL


@pytest.mark.parametrize(
    "url", ["/name/utopia", "/alpha/wat", "/currency/auf", "/region/mars", "/lang/elf"]
)
def test_invalid_returns_404(url):
    response = requests.get(f"{BASE_URL}{url}")
    data = response.json()
    assert response.status_code == 404
    assert data["message"] == "Not Found"
