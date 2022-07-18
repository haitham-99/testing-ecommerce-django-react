import pytest
from django.contrib import auth
from django.contrib.auth import get_user, logout
from django.contrib.auth.models import User
# from rest_framework.authtoken.admin import User
from django.test import client
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

client = APIClient()

'''
## Unit test - Testing if User can be created as a unit 
'''


@pytest.mark.django_db
def test_superuser_create():
    User.objects.create_superuser('test1', 'test1@test.com', 't1234567')
    count = User.objects.all().count()
    assert count == 1


def create_user():
    return User.objects.create(
        first_name='name',
        username='test_user@test.com',
        password='password',
    )


@pytest.mark.django_db
def test_create_user():
    U = create_user()
    assert isinstance(U, User) is True
    assert U.first_name == "name"


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="t1234567"
    )

    response = client.post("/api/users/register/", payload)

    data = response.data

    assert data["name"] == payload["name"]
    assert data["username"] == payload["email"]
    assert "password" not in data


@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True


# test delete use
@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")


@pytest.mark.django_db
def test_delete_created_user(user_1):
    user_1.delete()
    count = User.objects.all().count()
    assert count == 0


@pytest.mark.django_db
def test_change_user_first_name(user_1):
    user_data = User.objects.create_user(first_name="name", username='test1', email='test1@test.com',
                                            password='test1')  # username,email,password
    data = User.objects.get(user_data)
    print(data.first_name)
    data.first_name = 'test2'
    data.save()

    updated_user = User.objects.get(id=get_user.id)
    assert updated_user.first_name == "test2"


'''
## Api test - Integration Testing - testing if Api can create a user successfully 
'''


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
