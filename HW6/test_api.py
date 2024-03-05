import random

import pytest
import requests

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"


@pytest.fixture(scope='module')
def auth_token():
    authdata = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=authdata)
    token = response.json()["token"]
    yield token


@pytest.fixture(scope="session")
def booking_id():
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_url, json=payload)
    yield response.json()['bookingid']


@pytest.mark.smoke
def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code == 200


@pytest.mark.skip
def test_get_booking_by_id():
    response = requests.get(f'{base_url}/1')
    response_data = response.json()
    expected_keys = [
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
    ]
    assert response.status_code == 200
    print(response_data)
    print(len(response_data.keys()))
    assert len(response_data.keys()) == len(expected_keys)
    # for key in expected_keys:
    #     assert key in response_data.keys()


# def test_create_booking(booking_id):
#     response = requests.post(base_url,json=payload)
#     print(response.json()['bookingid'])
#     assert response.status_code == 200

@pytest.mark.regression
@pytest.mark.xfail(reason='wrong status code')
def test_check_created_booking(booking_id):
    result = requests.get(f"{base_url}/{booking_id}")
    print(result.json())
    assert result.status_code == 200
    assert result.json()['firstname'] == "James"


def test_update_booking(auth_token, booking_id):
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Lunch"
    }
    token = {"Cookie": f"token={auth_token}"}

    response = requests.put(f'{base_url}/{booking_id}', json=payload, headers=token)
    assert response.status_code == 200
    response_2 = requests.get(f'{base_url}/{booking_id}')
    print(response_2.json())
    assert response_2.json()["additionalneeds"] == "Lunch"


def test_patch_booking(auth_token, booking_id):
    name = random.choice(["Jonny", "Ann", "Alice", "Ira", "Oliver", "Tina"])
    price = random.choice([150, 20, 15, 100, 500, 1000, 50, 30, 80, 10_000_000])
    payload = {
        "firstname": name,
        "totalprice": price,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-02"
        },
        "additionalneeds": "Cookie, Breakfast"
    }
    token = {"Cookie": f"token={auth_token}"}
    response = requests.patch(f'{base_url}/{booking_id}', json=payload, headers=token)
    assert response.status_code == 200, \
        f"{response.status_code} is not 200"
    assert response.json()['firstname'] == name, \
        f"{response.json()['firstname']} is not {name}"
    assert response.json()['lastname'] == 'Brown', \
        f"{response.json()['firslastnametname']} is not 'Brown'"
    assert response.json()['totalprice'] == price, \
        f"{response.json()['totalprice']} is not {price}"
    assert not(response.json()['depositpaid']), \
        f"{response.json()['depositpaid']} is not 'False'"
    assert response.json()['bookingdates']['checkin'] == '2024-03-01', \
        f"{response.json()['bookingdates']['checkin']} is not '2024-03-01'"
    assert response.json()['bookingdates']['checkout'] == '2024-03-02', \
        f"{response.json()['bookingdates']['checkout']} is not '2024-03-02'"
    assert response.json()['additionalneeds'] == "Cookie, Breakfast", \
        f"{response.json()['additionalneeds']} is not 'Cookie, Breakfast'"

    response_get = requests.get(f'{base_url}/{booking_id}', json=payload, headers=token)
    assert response_get.status_code == 200, \
        f"{response_get.status_code} is not 200"
    assert response_get.json()['firstname'] == name, \
        f"{response_get.json()['firstname']} is not {name}"
    assert response_get.json()['lastname'] == 'Brown', \
        f"{response_get.json()['firslastnametname']} is not 'Brown'"
    assert response_get.json()['totalprice'] == price, \
        f"{response_get.json()['totalprice']} is not {price}"
    assert not(response_get.json()['depositpaid']), \
        f"{response_get.json()['depositpaid']} is not 'False'"
    assert response_get.json()['bookingdates']['checkin'] == '2024-03-01', \
        f"{response_get.json()['bookingdates']['checkin']} is not '2024-03-01'"
    assert response_get.json()['bookingdates']['checkout'] == '2024-03-02', \
        f"{response_get.json()['bookingdates']['checkout']} is not '2024-03-02'"
    assert response_get.json()['additionalneeds'] == "Cookie, Breakfast", \
        f"{response_get.json()['additionalneeds']} is not 'Cookie, Breakfast'"
    # print(response.json())


def test_delete_booking(booking_id, auth_token):
    token = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f'{base_url}/{booking_id}', headers=token)
    assert response.status_code == 201
    response_get = requests.get(f'{base_url}/{booking_id}')
    assert response_get.status_code == 404
