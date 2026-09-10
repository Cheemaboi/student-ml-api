import pytest

from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_health_returns_expected_v1_response(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "wrong",
        "application": "student-ml-api",
        "version": "1.0.0",
    }


def test_predict_doubles_valid_number(client):
    response = client.post("/predict", json={"value": 10})

    assert response.status_code == 200
    assert response.get_json() == {"input": 10, "prediction": 20}


def test_predict_rejects_missing_value(client):
    response = client.post("/predict", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "'value' is required"}


def test_predict_rejects_non_numeric_value(client):
    response = client.post("/predict", json={"value": "ten"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "'value' must be numeric"}
