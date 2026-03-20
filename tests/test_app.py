import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_task(client):
    response = client.post('/api/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task',
        'status': 'pending'
    })
    assert response.status_code == 201

def test_update_task(client):
    response = client.put('/api/tasks/1', json={
        'status': 'done'
    })
    assert response.status_code in [200, 404]

def test_delete_task(client):
    response = client.delete('/api/tasks/1')
    assert response.status_code in [200, 404]
