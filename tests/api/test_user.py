import pytest
from django.contrib import auth
from django.contrib.auth import get_user, logout
from django.contrib.auth.models import User
# from rest_framework.authtoken.admin import User
from django.test import client
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

'''
## Api test - Integration Testing - testing if Api can create a user successfully 
'''
client = APIClient()

@pytest.mark.django_db
def test_api_user_creation():
    payload = dict(name='test_user1@test.com', email='test_user1@test.com', password='t1234567')
    response = client.post("/api/users/register/", payload)

    payload = dict(username=response.data["username"], password='t1234567')
    response = client.post("/api/users/login/", payload)
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_login_user():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        username="test11",
        password="t1234567"
    )
    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", {"username": "test11@test.com", "password": "t1234567"})
    # print(response.data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():
    response = client.post("/api/users/login/", {"username": "test13@test.com", "password": "f1234567"})
    # UNAUTHORIZED 401
    assert response.status_code == 401


@pytest.mark.django_db
def test_if_profile_exist_after_login():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        username="test11",
        password="t1234567"
    )
    client.post("/api/users/register/", payload)
    client.post("/api/users/login/", {"username": "test11@test.com", "password": "t1234567"})
    response = client.get('http://127.0.0.1/#/profile')
    assert response.status_code == 200
