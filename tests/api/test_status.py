import pytest
from rest_framework.test import APIClient
from django.db import models
from rest_framework import status
client = APIClient()


@pytest.mark.django_db
def test_get_user_status_404():
    response = client.get("/api/status/0/")
    assert response.status_code == 404


# @pytest.mark.django_db
# def test_get_user():
#     payload = dict(
#         name="testing123",
#         email="test11@test.com",
#         password="t1234567"
#     )
#
#     st = status.objects.create(user_id=payload.id)
#     response = client.get("/api/status/0/")
#     assert response.status_code == 404
