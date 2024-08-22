import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

logging.basicConfig(filename='C:\\Users\\YourUsername\\Desktop\\test_search.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope='class')
def auth_token():
    url = "http://127.0.0.1:8080/auth"
    auth_data = HTTPBasicAuth('test_user', 'test_pass')
    response = requests.post(url, auth=auth_data)
    token = response.json().get("access_token")

    if not token:
        pytest.fail("Не вдалося отримати токен аутентифікації")

    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {token}'})
    return session


@pytest.mark.parametrize("sort_by, limit", [
    ('price', '5'),
    ('year', '3'),
    ('engine_volume', '7'),
    (None, '10'),
    ('brand', '2'),
    ('price', None),
    (None, None)
])
def test_search_cars(auth_token, sort_by, limit):
    url = "http://127.0.0.1:8080/cars"
    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    response = auth_token.get(url, params=params)
    logging.info(f"Request URL: {response.url}")
    logging.info(f"Response Status Code: {response.status_code}")
    logging.info(f"Response JSON: {response.json()}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if limit:
        assert len(response.json()) <= int(limit)

