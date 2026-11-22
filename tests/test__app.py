import pytest
from run import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.get_json() == {"status": "healthy"}

def test_chat_success(client):
    rv = client.post('/api/chat', json={"message": "Budget help"})
    assert rv.status_code == 200
    assert "response" in rv.get_json()

def test_empty_message(client):
    rv = client.post('/api/chat', json={"message": ""})
    assert rv.status_code == 400

def test_missing_message(client):
    rv = client.post('/api/chat', json={})
    assert rv.status_code == 400

def test_invalid_json(client):
    rv = client.post('/api/chat', data="not json", content_type='text/plain')
    assert rv.status_code == 400

def test_long_message(client):
    rv = client.post('/api/chat', json={"message": "A" * 501})
    assert rv.status_code == 400

def test_wrong_type(client):
    rv = client.post('/api/chat', json={"message": 123})
    assert rv.status_code == 400