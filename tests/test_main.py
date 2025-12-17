from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "git_hash" in data
    assert "full_git_hash" in data
    assert isinstance(data["git_hash"], str)
    assert len(data["git_hash"]) <= 7  # court ou "unknown"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "git_hash" in data
    assert isinstance(data["git_hash"], str)
    assert len(data["git_hash"]) <= 7
