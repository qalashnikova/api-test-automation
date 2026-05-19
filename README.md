# API Test Automation

![API Tests](https://github.com/qalashnikova/api-test-automation/actions/workflows/tests.yml/badge.svg)

Automated API tests for [REST Countries API](https://restcountries.com/) built with Python and pytest.

## Tech Stack

- Python 3.13
- pytest
- requests
- GitHub Actions (CI)

## Project Structure

tests/
├── countries_api/
│   ├── test_positive.py   # Positive scenarios for all endpoints
│   └── test_negative.py   # Negative scenarios (404, invalid inputs)
├── config.py              # Base URL configuration
└── conftest.py

## How to Run

Clone the repository and set up the environment:

```bash
git clone https://github.com/qalashnikova/api-test-automation.git
cd api-test-automation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run all tests:

```bash
pytest tests/
```

Run only positive or negative tests:

```bash
pytest tests/countries_api/test_positive.py
pytest tests/countries_api/test_negative.py
```

## Test Coverage

| Endpoint | Positive | Negative |
|---|---|---|
| `/alpha/{code}` | ✅ | ✅ |
| `/name/{name}` | ✅ | ✅ |
| `/region/{region}` | ✅ | ✅ |
| `/currency/{currency}` | ✅ | ✅ |
| `/lang/{language}` | ✅ | ✅ |
| `/all` | ✅ | — |