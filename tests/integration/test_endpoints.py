from fastapi.testclient import TestClient
from http import HTTPStatus


def test_genres_list(client: TestClient):
    response = client.get('/amazon/land_types')
    assert response.status_code == HTTPStatus.OK

    land_types = response.json()['land_types']
    assert isinstance(land_types, list)


def test_predict(client: TestClient, sample_image_bytes: bytes):
    files = {'image': sample_image_bytes}
    response = client.post('/amazon/predict', files=files)
    assert response.status_code == HTTPStatus.OK

    predicted_land_types = response.json()['land_types']
    assert isinstance(predicted_land_types, list)


def test_predict_proba(client: TestClient, sample_image_bytes: bytes):
    files = {'image': sample_image_bytes}
    response = client.post('/amazon/predict_proba', files=files)
    assert response.status_code == HTTPStatus.OK

    predcited_probs = response.json()
    for prob in predcited_probs.values():
        assert prob <= 1
