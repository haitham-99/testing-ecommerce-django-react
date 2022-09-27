import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_get_user_status_404():
    response = client.get("/api/status/0/")
    assert response.status_code == 404
