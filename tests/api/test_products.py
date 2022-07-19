import pytest
from django.contrib import auth
from django.contrib.auth import get_user, logout
from django.contrib.auth.models import User
# from rest_framework.authtoken.admin import User
from django.test import client
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


# Api test  - Integration testing
@pytest.mark.django_db
def test_api_product_creation():
    client = APIClient()
    user = User.objects.create_superuser(username='testuser', password='134')
    client.force_authenticate(user)
    response = client.post("/api/products/create/")
    assert response.status_code == 200



