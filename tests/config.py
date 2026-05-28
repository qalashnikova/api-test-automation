import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://restcountries.com/v3.1"
REQRES_BASE_URL = "https://reqres.in/api"
REQRES_API_KEY = os.getenv("REQRES_API_KEY")
