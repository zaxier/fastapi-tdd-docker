# project/tests/test_ping.py

from app import main


def test_ping(test_app):
    # Given
    # test_app = TestClient(main.app)

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "ping": "pong!",
        "environment": "dev",
        "testing": True,
        "zaxier": "awesome",
    }
