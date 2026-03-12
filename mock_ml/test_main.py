from fastapi.testclient import TestClient
from unit_test.mock import patch
from main import app

client = TestClient()