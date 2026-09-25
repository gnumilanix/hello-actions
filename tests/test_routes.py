from greetings import app


def test_hello_world_returns_message():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello World'}


def test_hello_world_rejects_post():
    client = app.test_client()

    response = client.post('/')

    assert response.status_code == 405