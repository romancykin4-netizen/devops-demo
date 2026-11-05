from app.main import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from DevOps demo!"


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_metrics():
    app.test_client().get("/")
    response = app.test_client().get("/metrics")
    assert response.status_code == 200
    assert b"app_requests_total" in response.data
