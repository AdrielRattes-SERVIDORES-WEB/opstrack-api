import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok", "service": "opstrack-api"}


def test_status(client):
    resp = client.get("/status")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "operational"


def test_tickets(client):
    resp = client.get("/tickets")
    assert resp.status_code == 200
    tickets = resp.get_json()["tickets"]
    assert len(tickets) == 3
    assert {t["status"] for t in tickets} == {"aberto", "em andamento", "fechado"}


def test_sobre(client):
    resp = client.get("/sobre")
    assert resp.status_code == 200
    assert resp.get_json() == {"nome": "OpsTrack API", "versao": "0.1.0"}
