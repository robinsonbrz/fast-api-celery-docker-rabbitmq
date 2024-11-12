# conftest.py
import pytest
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:8000")

@pytest.fixture
def sget(base_url):
    # sget function to simplify GET requests
    def _sget(endpoint, params=None):
        return requests.get(f"{base_url}{endpoint}", params=params)
    return _sget

@pytest.fixture
def spost(base_url):
    # spost function to simplify POST requests
    def _spost(endpoint, data=None, json=None):
        return requests.post(f"{base_url}{endpoint}", data=data, json=json)
    return _spost
