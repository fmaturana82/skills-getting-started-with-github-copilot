from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant():
    response = client.delete(
        "/activities/Chess%20Club/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]

    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]

def test_get_activities():
    client = TestClient(app)
    response = client.get("/activities")

    assert response.status_code == 200
    assert "Chess Club" in response.json()