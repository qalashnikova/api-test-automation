# API Test Automation

![API Tests](https://github.com/qalashnikova/api-test-automation/actions/workflows/tests.yml/badge.svg)

Automated API tests for [REST Countries API](https://restcountries.com/) and [Reqres API](https://reqres.in/) built with Python and pytest.

## Tech Stack

- Python 3.13
- pytest
- requests
- python-dotenv
- GitHub Actions (CI)

## Project Structure

```
tests/
├── countries_api/
│   ├── test_positive.py   # Positive scenarios for all endpoints
│   └── test_negative.py   # Negative scenarios (404, invalid inputs)
├── reqres_api/
│   ├── test_users.py      # List, single, create, update, delete users
│   ├── test_auth.py       # Login and token generation
│   └── test_register.py   # Successful and unsuccessful registration
├── config.py              # Base URL configuration
└── conftest.py
```

## How to Run

Clone the repository and set up the environment:

```bash
git clone https://github.com/qalashnikova/api-test-automation.git
cd api-test-automation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the root of the project:

```
REQRES_API_KEY=your_api_key_here
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

Run only Reqres tests:

```bash
pytest tests/reqres_api/
```

## Test Coverage

### REST Countries API

| Endpoint | Positive | Negative |
|---|---|---|
| `/alpha/{code}` | ✅ | ✅ |
| `/name/{name}` | ✅ | ✅ |
| `/region/{region}` | ✅ | ✅ |
| `/currency/{currency}` | ✅ | ✅ |
| `/lang/{language}` | ✅ | ✅ |
| `/all` | ✅ | — |

### Reqres API

| Endpoint | Method | Tests |
|---|---|---|
| `/users` | GET | ✅ |
| `/users/{id}` | GET | ✅ |
| `/users` | POST | ✅ |
| `/users/{id}` | PUT | ✅ |
| `/users/{id}` | PATCH | ✅ |
| `/users/{id}` | DELETE | ✅ |
| `/login` | POST | ✅ |
| `/register` | POST | ✅ |
