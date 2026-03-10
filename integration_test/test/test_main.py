from fastapi.testclient import TestClient
from integration_test.app.main import app

client =TestClient(app)
