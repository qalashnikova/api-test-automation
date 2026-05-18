import requests
import json


response = requests.get("https://restcountries.com/v3.1/alpha/th")
# print(response.status_code)
# print(response.json())
# print(response.headers)
# print(json.dumps(response.json(), indent=2))

data = response.json()
country = data[0]  # первый элемент списка
print(country["capital"][0])
# print(json.dumps(country["capital"], indent=2))

print(country["name"]["common"])
